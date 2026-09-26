# INDIVIDUAL STOCK CHATGPT PACKET - 5475 德宏

## Metadata
- generated_at: 2026-09-26 22:17:10 Asia/Taipei
- stock_id: 5475
- stock_name: 德宏
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5475_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5475_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5475_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5475_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5475_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5475_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5475_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5475_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5475_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5475_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5475_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5475_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5475.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5475.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5475.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5475.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5475_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5475_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5475_latest.md?ref=main

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
- open: 175.5
- high: 183
- low: 175
- close: 181
- volume: 2770000
- ma5: 179.4
- ema23_primary: 179
- distance_to_ema23_pct: 1.12
- ma20: 185.07
- ma60: 169.13
- ma120: 234.27
- return_5d: 5.54
- return_20d: -9.05
- volume_ratio: 0.46
- distance_to_ma20_pct_auxiliary: -2.2
- distance_to_high_60_pct: -25.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,207.5,212.5,197.5,201,18108000,168.5,19.28,158.22,191.06,2.27
20260831,197,215,196.5,204.5,9008000,171.5,19.24,162.35,189.42,1.07
20260901,206,212.5,198,200.5,6204000,173.92,15.28,165.68,188.08,0.73
20260902,195.5,204.5,190,190,4974000,175.26,8.41,168.95,186.99,0.6
20260903,192,208.5,181,182.5,6874000,175.86,3.77,171.93,185.68,0.83
20260904,188,190,176,190,5443000,177.04,7.32,175.25,184.77,0.66
20260907,192,198,190,194,4316000,178.45,8.71,178.7,184.03,0.52
20260908,195,196,185,190,2998000,179.42,5.9,181.45,183.2,0.39
20260909,190,203.5,188.5,193,5675000,180.55,6.9,183.68,182.44,0.79
20260910,193,194.5,184,184.5,3837000,180.88,2,184.75,181.68,0.62
20260911,181,196,175,175,8126000,180.39,-2.99,184.97,180.77,1.56
20260914,172.5,181.5,171,176,4592000,180.02,-2.23,185.32,179.5,0.86
20260915,173,179.5,169.5,170,3566000,179.19,-5.13,184.7,177.72,0.68
20260916,171.5,186,171.5,182,5394000,179.42,1.44,184.8,176.1,0.99
20260917,183.5,188.5,168,171.5,7461000,178.76,-4.06,184.57,174.36,1.3
20260918,175,180,171.5,179,7812000,178.78,0.12,184.8,172.86,1.29
20260921,179,179,174.5,179,2252000,178.8,0.11,185.78,171.8,0.37
20260922,188.5,195,179.5,181,8701000,178.98,1.13,186.18,171.07,1.35
20260923,183,183.5,175,177,2280000,178.82,-1.02,185.97,169.95,0.35
20260924,175.5,183,175,181,2770000,179,1.12,185.07,169.13,0.46
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 22.8
- over_600_ratio: 20.1
- over_800_ratio: 19.08
- over_1000_ratio: 19.08
- over_400_change_1w: -0.85
- over_800_change_1w: 0.42
- over_1000_change_1w: 1.15
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,40.42,1.01,35.43,0.46,33.94,-1.03,1,False,True
20260717,41.29,0.87,34.61,-0.82,34.61,0.67,2,False,True
20260724,42.36,1.07,36.19,1.58,36.19,1.58,3,True,True
20260731,44.31,1.95,40.13,3.94,38.67,2.48,4,True,True
20260807,39.73,-4.58,35.87,-4.26,35.17,-3.5,0,False,False
20260814,31.91,-7.82,28.65,-7.22,26.67,-8.5,0,False,False
20260821,28.91,-3,24.18,-4.47,23.55,-3.12,0,False,False
20260828,28.78,-0.13,24.71,0.53,23.2,-0.35,1,False,True
20260904,26.93,-1.85,21.7,-3.01,21.7,-1.5,0,False,False
20260911,25.82,-1.11,21.47,-0.23,20.78,-0.92,0,False,False
20260918,23.65,-2.17,18.66,-2.81,17.93,-2.85,0,False,False
20260924,22.8,-0.85,19.08,0.42,19.08,1.15,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 5475 | 德宏 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/09/21 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: (1)單月                 最近一月單月  去年同月    與去年同期增減%                   (115/08)    (114/08) --------------------------------------------------------------- 營業收入(百萬)      255          68         271.88 稅前淨利(百萬)       95          -4       2,684.83 歸屬母公司 業主淨利(百萬)       95          -4       2,684.83 每股盈餘 (元)      0.74       -0.03       2,684.83 =============================================================== (2)單季              最近一季單季      去年同期     與去年同期增減%              (115年第2季)    (114年第2季) --------------------------------------------------------------- 營業收入(百萬)     511           197        159.31 稅前淨利(百萬)     121           -15        891.51 歸屬母公司 業主淨利(百萬)     121           -15        891.51 每股盈餘 (元)     0.95         -0.12        891.51 ================================================================ (3)最近四季累計                114年第3季至115年第2季 ---------------------------------------------------------------- 營業收入(百萬)        1,341 稅前淨利(百萬)          168 歸屬母公司 業主淨利(百萬)          164 每股盈餘 (元)          1.29 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註：以上115年08月及去年同期比較數之財務資料係本公司採IFRS會     計準則編製之合併數，未經會計師查核(閱)，僅供投資人參考。 註：最近一季115年第2季係指單季數字，非為最近財務報告中之累計     數字，且係本公司採IFRS下編製之合併數，業經會計師查核(閱)，     僅供投資人參考。 註：最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併     數，業經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 5475 | 德宏 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/09/21 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: (1)單月                 最近一月單月  去年同月    與去年同期增減%                   (115/08)    (114/08) --------------------------------------------------------------- 營業收入(百萬)      255          68         271.88 稅前淨利(百萬)       95          -4       2,684.83 歸屬母公司 業主淨利(百萬)       95          -4       2,684.83 每股盈餘 (元)      0.74       -0.03       2,684.83 =============================================================== (2)單季              最近一季單季      去年同期     與去年同期增減%              (115年第2季)    (114年第2季) --------------------------------------------------------------- 營業收入(百萬)     511           197        159.31 稅前淨利(百萬)     121           -15        891.51 歸屬母公司 業主淨利(百萬)     121           -15        891.51 每股盈餘 (元)     0.95         -0.12        891.51 ================================================================ (3)最近四季累計                114年第3季至115年第2季 ---------------------------------------------------------------- 營業收入(百萬)        1,341 稅前淨利(百萬)          168 歸屬母公司 業主淨利(百萬)          164 每股盈餘 (元)          1.29 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註：以上115年08月及去年同期比較數之財務資料係本公司採IFRS會     計準則編製之合併數，未經會計師查核(閱)，僅供投資人參考。 註：最近一季115年第2季係指單季數字，非為最近財務報告中之累計     數字，且係本公司採IFRS下編製之合併數，業經會計師查核(閱)，     僅供投資人參考。 註：最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併     數，業經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 5475 | 德宏 | 19 | 16 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
