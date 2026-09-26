# INDIVIDUAL STOCK CHATGPT PACKET - 3374 精材

## Metadata
- generated_at: 2026-09-26 15:51:56 Asia/Taipei
- stock_id: 3374
- stock_name: 精材
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3374_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3374_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3374_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3374_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3374_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3374_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3374_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3374_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3374_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3374_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3374_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3374_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3374.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3374.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3374.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3374.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3374_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3374_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3374_latest.md?ref=main

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
- date: 20260924
- open: 462.5
- high: 464.5
- low: 442
- close: 449
- volume: 14226000
- ma5: 459.1
- ema23_primary: 424.92
- distance_to_ema23_pct: 5.67
- ma20: 442.02
- ma60: 367.14
- ma120: 299.52
- return_5d: 4.66
- return_20d: 27.92
- volume_ratio: 1.11
- distance_to_ma20_pct_auxiliary: 1.58
- distance_to_high_60_pct: -9.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,352,386,350,386,28788000,324.23,19.05,319.62,309.05,1.87
20260831,390.5,424.5,388.5,422.5,41562000,332.42,27.1,325.52,311.86,2.41
20260901,422.5,431,412,421.5,21935000,339.84,24.03,331.12,314.77,1.26
20260902,418,430,413,419.5,3650000,346.48,21.07,336.45,317.88,0.22
20260903,420,424,393,400,4513000,350.94,13.98,340.65,320.53,0.27
20260904,420,430,403,430,4668000,357.53,20.27,346.82,323.96,0.29
20260907,448,472.5,436,469.5,4538000,366.86,27.98,353.45,328.07,0.28
20260908,474,482.5,456,475,3377000,375.87,26.37,360.5,332.1,0.22
20260909,471,487,471,478.5,2339000,384.42,24.47,367.93,336.07,0.16
20260910,481,494,476,488,2996000,393.06,24.16,376.07,340.3,0.21
20260911,472,496,463,463.5,15121000,398.93,16.19,383,343.95,1.07
20260914,440,447.5,417.5,429.5,17313000,401.47,6.98,389.85,346.93,1.21
20260915,429,430.5,407,408.5,7868000,402.06,1.6,394.95,349.13,0.59
20260916,417,436,410.5,424,12851000,403.89,4.98,401.2,351.14,0.95
20260917,429,445,423,429,12866000,405.98,5.67,407.48,353.09,1.01
20260918,440,444.5,418.5,444.5,13489000,409.19,8.63,414.38,355.48,1.06
20260921,451.5,456,432,443,9732000,412.01,7.52,421.4,358.2,0.76
20260922,465,487,459,487,16778000,418.26,16.44,430.2,361.63,1.27
20260923,486,486,463,472,17529000,422.74,11.65,437.12,364.73,1.33
20260924,462.5,464.5,442,449,14226000,424.92,5.67,442.02,367.14,1.11
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 67.77
- over_600_ratio: 66.29
- over_800_ratio: 64.79
- over_1000_ratio: 64.17
- over_400_change_1w: -0.07
- over_800_change_1w: 0.12
- over_1000_change_1w: -0.5
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,63.57,2.83,60.96,2.49,60.31,2.52,4,True,True
20260717,64.97,1.4,62.95,1.99,61.66,1.35,5,True,True
20260724,65.66,0.69,63.65,0.7,62.35,0.69,6,True,True
20260731,63.42,-2.24,60.72,-2.93,60.05,-2.3,0,False,False
20260807,62.9,-0.52,60.51,-0.21,59.79,-0.26,1,False,False
20260814,61,-1.9,58.64,-1.87,57.54,-2.25,0,False,False
20260821,58.19,-2.81,55.1,-3.54,54.14,-3.4,0,False,False
20260828,60.82,2.63,57.35,2.25,56.05,1.91,1,True,True
20260904,66.76,5.94,63.56,6.21,62.2,6.15,2,True,True
20260911,69.03,2.27,65.83,2.27,64.83,2.63,3,True,True
20260918,67.84,-1.19,64.67,-1.16,64.67,-0.16,0,False,False
20260924,67.77,-0.07,64.79,0.12,64.17,-0.5,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3374 | 精材 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | stale_signal | 1.事實發生日:115/09/21 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知處理及辦理公告。 3.財務業務資訊:   單月(註1)                115年8月    114年8月    與去年同期增減%(註4)   營業收入(百萬元)            909         665           +37%   稅前純益(百萬元)            239         167           +43%   歸屬母公司業主淨利(百萬元)  193         135           +43%   稅後每股盈餘(元)           0.71        0.50           +42%    單季(註2)               115年第2季  114年第2季   與去年同期增減%(註4)   營業收入(百萬元)           2185        1537           +42%   稅前純益(百萬元)            487          72          +576%   歸屬母公司業主淨利(百萬元)  396          65          +509%   稅後每股盈餘(元)           1.46        0.24          +508%    最近四季累計(註3)    114年第3季至115年第2季   營業收入(百萬元)             8255   稅前純益(百萬元)             2078   歸屬母公司業主淨利(百萬元)   1727   稅後每股盈餘(元)             6.37   公司每股面額:10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項:   註1：以上115年8月及去年同期比較數之財務資料係本公司採IFRS會計準則編製        之自結數，未經會計師查核(閱)，僅供投資人參考。   註2：最近一季115年第2季係指單季數字，係本公司採IFRS會計準則下編製之個        別財報數，業經會計師核閱，僅供投資人參考。   註3：最近四季累計係本公司114年第3季至115年第2季採IFRS編製之個別財報數，        業經會計師查核(閱)，僅供投資人參考。   註4：與去年同期增減% = (本期 - 去年同期) / 去年同期絕對值；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 3374 | 精材 | revenue_pullback | 營收成長股價回檔 | 76.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/09/21 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知處理及辦理公告。 3.財務業務資訊:   單月(註1)                115年8月    114年8月    與去年同期增減%(註4)   營業收入(百萬元)            909         665           +37%   稅前純益(百萬元)            239         167           +43%   歸屬母公司業主淨利(百萬元)  193         135           +43%   稅後每股盈餘(元)           0.71        0.50           +42%    單季(註2)               115年第2季  114年第2季   與去年同期增減%(註4)   營業收入(百萬元)           2185        1537           +42%   稅前純益(百萬元)            487          72          +576%   歸屬母公司業主淨利(百萬元)  396          65          +509%   稅後每股盈餘(元)           1.46        0.24          +508%    最近四季累計(註3)    114年第3季至115年第2季   營業收入(百萬元)             8255   稅前純益(百萬元)             2078   歸屬母公司業主淨利(百萬元)   1727   稅後每股盈餘(元)             6.37   公司每股面額:10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項:   註1：以上115年8月及去年同期比較數之財務資料係本公司採IFRS會計準則編製        之自結數，未經會計師查核(閱)，僅供投資人參考。   註2：最近一季115年第2季係指單季數字，係本公司採IFRS會計準則下編製之個        別財報數，業經會計師核閱，僅供投資人參考。   註3：最近四季累計係本公司114年第3季至115年第2季採IFRS編製之個別財報數，        業經會計師查核(閱)，僅供投資人參考。   註4：與去年同期增減% = (本期 - 去年同期) / 去年同期絕對值；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3374 | 精材 | 7 | 2 | 5 | 7 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
