# INDIVIDUAL STOCK CHATGPT PACKET - 3090 日電貿

## Metadata
- generated_at: 2026-09-05 15:53:11 Asia/Taipei
- stock_id: 3090
- stock_name: 日電貿
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 347
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3090_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3090_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3090.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3090.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3090.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3090.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3090_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3090_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3090_latest.md?ref=main

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
- date: 20260904
- open: 167.5
- high: 177
- low: 167.5
- close: 176.5
- volume: 12141957
- ma5: 171.1
- ema23_primary: 171.39
- distance_to_ema23_pct: 2.98
- ma20: 169.5
- ma60: 213.92
- ma120: 174.69
- return_5d: 1.44
- return_20d: 17.28
- volume_ratio: 0.98
- distance_to_ma20_pct_auxiliary: 4.13
- distance_to_high_60_pct: -51.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,158,165.5,155.5,161,12014907,177.64,-9.37,164.38,225.77,1.65
20260811,158,177,158,174.5,32414204,177.38,-1.62,161.47,226.31,3.91
20260812,175.5,177,168,170.5,20350162,176.8,-3.56,158.75,226.68,2.31
20260813,173.5,187,173.5,175,21500770,176.65,-0.94,157.05,226.89,2.31
20260814,179.5,181,170.5,174.5,12877678,176.47,-1.12,156.05,226.82,1.41
20260817,171,171,163.5,166,8823467,175.6,-5.47,155.57,226.32,0.93
20260818,167,168.5,161,161.5,5949576,174.43,-7.41,154.88,225.43,0.62
20260819,158,177.5,158,177.5,21470953,174.68,1.61,154.6,224.45,2.04
20260820,186,187,169.5,172,22502808,174.46,-1.41,154.62,223.45,1.95
20260821,175.5,177,164,165,9808733,173.67,-4.99,154.68,222.35,0.82
20260824,164.5,169,163,163,3998293,172.78,-5.66,155.03,221.59,0.33
20260825,162,166,157.5,166,4214058,172.22,-3.61,156.3,220.54,0.35
20260826,166,167,162,165.5,3412028,171.66,-3.59,158.25,219.41,0.28
20260827,168.5,172,164,168.5,8767327,171.39,-1.69,160.97,218.55,0.7
20260828,175.5,184,171.5,174,19371638,171.61,1.39,163.43,217.88,1.45
20260831,172,178.5,167,175,9614767,171.89,1.81,165.3,217.12,0.72
20260901,172,179.5,172,173,9067944,171.98,0.59,166.75,216.32,0.71
20260902,170,170.5,168,168.5,3121980,171.69,-1.86,167.82,215.63,0.25
20260903,169,172,162.5,162.5,5160663,170.93,-4.93,168.2,214.51,0.42
20260904,167.5,177,167.5,176.5,12141957,171.39,2.98,169.5,213.92,0.98
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 61.03
- over_600_ratio: 57.93
- over_800_ratio: 56.76
- over_1000_ratio: 54.87
- over_400_change_1w: -0.5
- over_800_change_1w: -0.76
- over_1000_change_1w: -1.13
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,69.35,1,64.07,0.07,62.53,1.01,5,True,True
20260626,69.17,-0.18,64.4,0.33,62.57,0.04,6,False,True
20260703,69.36,0.19,64.48,0.08,62.67,0.1,7,False,True
20260709,69.19,-0.17,63.78,-0.7,62.28,-0.39,0,False,False
20260717,69.06,-0.13,63.67,-0.11,62.16,-0.12,0,False,False
20260724,68.49,-0.57,63.62,-0.05,61.76,-0.4,0,False,False
20260731,67.45,-1.04,63.08,-0.54,61.87,0.11,1,False,True
20260807,65.74,-1.71,60.7,-2.38,59.49,-2.38,0,False,False
20260814,62.26,-3.48,56.9,-3.8,54.76,-4.73,0,False,False
20260821,62.56,0.3,57.6,0.7,56.38,1.62,1,True,True
20260828,61.53,-1.03,57.52,-0.08,56,-0.38,0,False,False
20260904,61.03,-0.5,56.76,-0.76,54.87,-1.13,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3090 | 日電貿 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/07/16 2.發生緣由:依台灣證券交易所通知辦理。 3.財務業務資訊: 本公司合併財務資訊： 期 間        最近一月     與去年同期   最近一季     與去年同期   最近四季累計 　　         (115年6月)     增 減 %   (115年第2季)   增 減 %   114年第3季至 　　　　　　　　　　　　　　　　　　　　　　                     115年第2季 科 目　    (IFRS合併自結數)　　  　　(IFRS合併自結數)        (IFRS合併自結數) =======   =============== ======== =============== ======== ================ 營業收入　        1681　     32.36　　     5154       26.76          17512 (百萬) 稅前淨利           639     1152.94　　     1036      524.10           2630 (百萬) 歸屬母公司業主淨利  596　   1555.56　　      909      663.87           2173 (百萬) 每股盈餘          2.07　   1117.65　　     3.16      464.29           8.11 (元)  4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項: 註1：每股盈餘除最近一月及去年同期以及最近一季係依普通股期末股數計算外，      餘係依普通股加權平均股數計算，最近一月(115年6月)及去年同期(114年6月)      係分別依287,567仟股及212,597仟股計算；最近一季(115年第2季)及      去年同期(114年第2季)係分別依287,567仟股及210,353仟股計算；      最近四季累計(114年第3季至115年第2季)係依114年228,734仟股、      115年第1季282,583仟股及115年第2季287,567仟股計算之數值相加。  註2：本公司115年6月及115年第2季合併自結數皆認列股利收入457百萬元。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3090 | 日電貿 | 5 | 1 | 5 | 7 | 14 | repeated_but_no_breakout | 近 10 日上榜 7 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3090 | 日電貿 | 65 | 0 | 7773840.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
