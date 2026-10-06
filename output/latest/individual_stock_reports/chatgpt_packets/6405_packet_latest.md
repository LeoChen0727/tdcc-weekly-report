# INDIVIDUAL STOCK CHATGPT PACKET - 6405 悅城

## Metadata
- generated_at: 2026-10-06 22:18:33 Asia/Taipei
- stock_id: 6405
- stock_name: 悅城
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 366
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6405_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6405_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6405_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6405_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6405_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6405_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6405_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6405_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6405_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6405_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6405_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6405_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6405.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6405.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6405.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6405.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6405_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6405_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6405_latest.md?ref=main

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
- date: 20261002
- open: 41.9
- high: 43.05
- low: 41.25
- close: 42.5
- volume: 3961514
- ma5: 44.94
- ema23_primary: 41.79
- distance_to_ema23_pct: 1.7
- ma20: 40.88
- ma60: 41.05
- ma120: 50.09
- return_5d: 2.29
- return_20d: 0.59
- volume_ratio: 4.37
- distance_to_ma20_pct_auxiliary: 3.96
- distance_to_high_60_pct: -26.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,42.25,42.25,39.1,39.2,1088439,40.48,-3.17,39.69,48.45,2.14
20260904,39.25,41.4,39.25,40.1,650887,40.45,-0.87,39.78,47.96,1.25
20260907,40.1,40.6,39.1,39.2,491523,40.35,-2.84,39.74,47.4,0.96
20260908,39.35,39.8,38.65,38.65,416013,40.21,-3.87,39.65,46.88,0.82
20260909,39.2,40.35,38.7,38.9,479029,40.1,-2.98,39.55,46.49,0.94
20260910,38.9,39.2,38.25,39.2,207959,40.02,-2.05,39.48,46.16,0.41
20260911,37.1,38.55,37.1,38.35,282207,39.88,-3.84,39.4,45.72,0.55
20260914,37.35,38.4,37.2,37.6,172239,39.69,-5.27,39.3,45.15,0.34
20260915,37.55,37.9,37.1,37.1,143069,39.48,-6.02,39.23,44.63,0.29
20260916,37.25,38.05,37.25,37.6,285607,39.32,-4.37,39.19,44.12,0.57
20260917,37.6,41.35,37.6,41.35,610708,39.49,4.71,39.32,43.66,1.18
20260918,41.75,42.15,40,40.6,1879987,39.58,2.57,39.4,43.25,3.12
20260921,40.3,42.25,40.3,41.6,925436,39.75,4.65,39.57,42.94,1.47
20260922,41.6,44.5,41.4,41.95,1641771,39.93,5.05,39.77,42.62,2.34
20260923,42,43.8,41.1,41.55,760808,40.07,3.7,39.77,42.3,1.07
20260924,40.6,42.8,40.6,41.45,538439,40.18,3.15,39.83,42,0.8
20260929,41.1,45.55,40.95,45.55,1486305,40.63,12.11,40.09,41.75,2.03
20260930,50.1,50.1,50.1,50.1,470287,41.42,20.96,40.65,41.55,0.63
20261001,45.1,45.1,45.1,45.1,1637248,41.73,8.09,40.87,41.28,2.03
20261002,41.9,43.05,41.25,42.5,3961514,41.79,1.7,40.88,41.05,4.37
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 50.3
- over_600_ratio: 45.26
- over_800_ratio: 43.16
- over_1000_ratio: 36.65
- over_400_change_1w: -1.47
- over_800_change_1w: -1.8
- over_1000_change_1w: -0.26
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,52.47,0.16,43.48,-1.2,36.71,-1.42,3,False,False
20260724,52.69,0.22,43.37,-0.11,36.66,-0.05,4,False,False
20260731,53.8,1.11,42.88,-0.49,37.6,0.94,5,False,True
20260807,52.9,-0.9,42.83,-0.05,37.55,-0.05,0,False,False
20260814,53.55,0.65,44.57,1.74,39.29,1.74,1,True,True
20260821,53.24,-0.31,42.96,-1.61,37.68,-1.61,2,False,False
20260828,52.81,-0.43,43.14,0.18,37.86,0.18,3,False,True
20260904,52.43,-0.38,42.9,-0.24,37.62,-0.24,0,False,False
20260911,52.39,-0.04,44.09,1.19,37.56,-0.06,1,False,True
20260918,52.2,-0.19,43.92,-0.17,37.41,-0.15,0,False,False
20260924,51.77,-0.43,44.96,1.04,36.91,-0.5,1,False,True
20261002,50.3,-1.47,43.16,-1.8,36.65,-0.26,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6405 | 悅城 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | stale_signal | 1.事實發生日:115/10/01 2.公司名稱:悅城科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:投資網誌,財訊快報及相關自媒體 6.報導內容:摘錄自媒體報導如下:  (1)投資網誌:...估值方面，機構預估今年每股稅後 EPS 為 -1.06 元，...  (2)財訊快報:...還有原先專職面板玻璃基板加工，如薄化、蝕刻，現在     轉入氮化鋁（AlN）與玻璃減薄單製程，並以台積電為目標客戶的供應商悅城。 7.發生緣由:大眾傳播媒體報導 8.因應措施:  (1)由於玻璃薄化產業快速變遷，致使本公司長期虧損，已於114年結束與玻璃     相關製程，包含玻璃基板、TGV、CPO、玻璃加工、玻璃鍍膜...等與玻璃相     關產品。  (2)該報導所提為自媒體自行推估與臆測，本公司並未提供財務預測或預測性     財務及客戶資訊，有關本公司營運資訊，悉以公開資訊觀測站公佈之資料     為準，特此澄清。 9.其他應敘明事項:  (1)任何蓄意散佈不實謠言意圖影響股價，損及本公司商譽與破壞市場秩序者，     本公司將報請主管機關依法追究，絕不寬貸。   (2)有關本公司營運情形、營收及獲利狀況均依規定公告於公開資訊觀測站，     投資人應以本公司經會計師查核簽證並依法公告之資訊為依據，以免損及     自身權益。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6405 | 悅城 | 2 | 2 | 3 | 4 | 5 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
