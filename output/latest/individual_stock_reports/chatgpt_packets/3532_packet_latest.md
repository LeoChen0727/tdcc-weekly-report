# INDIVIDUAL STOCK CHATGPT PACKET - 3532 台勝科

## Metadata
- generated_at: 2026-08-01 22:27:31 Asia/Taipei
- stock_id: 3532
- stock_name: 台勝科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 315
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3532_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3532_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3532_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3532_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3532_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3532_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3532_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3532_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3532_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3532_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3532_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3532_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3532.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3532.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3532.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3532.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3532_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3532_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3532_latest.md?ref=main

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
- date: 20260730
- open: 277.5
- high: 294
- low: 277.5
- close: 277.5
- volume: 6889612
- ma5: 337.3
- ema23_primary: 387.52
- distance_to_ema23_pct: -28.39
- ma20: 416.9
- ma60: 339.84
- ma120: 245.2
- return_5d: -34.16
- return_20d: -30.62
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: -33.44
- distance_to_high_60_pct: -49.73

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,399,414.5,394,407,1366375,342.48,18.84,344.27,265.32,0.52
20260703,393.5,443.5,393.5,440,992601,350.61,25.5,351.73,270.3,0.38
20260706,455,484,406,406,16088077,355.23,14.29,357.52,274.56,4.72
20260707,410.5,429,376,383,9309818,357.54,7.12,363.62,278.18,2.41
20260708,387,420,375.5,409.5,6900168,361.87,13.16,369.88,281.98,1.66
20260709,415,450,408.5,423.5,9076182,367.01,15.39,377.55,286.05,1.98
20260713,465.5,465.5,465.5,465.5,1362260,375.21,24.06,385.98,290.58,0.3
20260714,459,510,430.5,510,19185008,386.45,31.97,395.15,295.85,3.88
20260715,535,552,506,523,15236731,397.83,31.46,403.35,301.43,2.75
20260716,504,519,471,471,7815331,403.92,16.61,407.18,306.18,1.35
20260717,424,470,424,424,9795006,405.6,4.54,408.6,310.2,1.77
20260720,434,466,401,466,12923121,410.63,13.48,412.4,314.85,2.22
20260721,470,470,432,433.5,18628212,412.54,5.08,415.15,319.22,2.78
20260722,446.5,476.5,440.5,468,14308280,417.16,12.19,419.9,324.14,1.94
20260723,472,499,421.5,421.5,14814207,417.52,0.95,422.73,328.13,1.83
20260724,405,410,379.5,379.5,7975692,414.35,-8.41,423.1,331.49,0.94
20260727,372,380.5,357.5,379.5,6707709,411.45,-7.76,425.27,334.79,0.77
20260728,350,355.5,342,342,3830521,405.66,-15.69,425.82,337.34,0.43
20260729,337,339.5,308,308,2899952,397.52,-22.52,423.02,339.02,0.32
20260730,277.5,294,277.5,277.5,6889612,387.52,-28.39,416.9,339.84,0.74
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 90.1
- over_600_ratio: 88.4
- over_800_ratio: 87.89
- over_1000_ratio: 87.16
- over_400_change_1w: 0.09
- over_800_change_1w: 0.16
- over_1000_change_1w: 0.42
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,90.75,-0.02,88.79,0.12,88.3,0.57,2,False,True
20260522,90.71,-0.04,88.62,-0.17,88.11,-0.19,3,False,False
20260529,91.31,0.6,89.18,0.56,88.23,0.12,4,True,True
20260605,91.26,-0.05,89.18,0,88.47,0.24,5,False,True
20260612,91.36,0.1,88.95,-0.23,87.98,-0.49,6,False,False
20260618,91.57,0.21,89.29,0.34,88.78,0.8,7,False,True
20260626,91.26,-0.31,89.04,-0.25,88.28,-0.5,8,False,False
20260703,91.16,-0.1,88.93,-0.11,88.46,0.18,9,False,True
20260709,90.97,-0.19,89.24,0.31,88.06,-0.4,10,False,True
20260717,90.98,0.01,88.27,-0.97,87.12,-0.94,11,False,False
20260724,90.01,-0.97,87.73,-0.54,86.74,-0.38,0,False,False
20260731,90.1,0.09,87.89,0.16,87.16,0.42,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3532 | 台勝科 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/06/17 2.發生緣由:依臺灣證券交易所股份有限公司通知辦理 3.財務業務資訊:(IFRS合併) 單位:新台幣佰萬元     最近一月          與去年同期 科目                   (115年5月自結數)        增減% ----------------------------------------------------- 營業收入                     1,218               +24.43% 稅前淨利                       -26               +81.56% 歸屬母公司業主淨利             -26               +81.56% 每股盈餘(元)                 -0.07               +81.56%  單位:新台幣佰萬元     最近一季          與去年同期                          (115年第1季核閱數)        增減% 科目 ----------------------------------------------------- 營業收入                     3,309              +10.87% 稅前淨利                       -82              -127.43% 歸屬母公司業主淨利             -68              -128.61% 每股盈餘(元)                 -0.18              -128.61%  科目             最近四季累計(114年第2季至115年第1季查核數) ----------------------------------------------------- 營業收入(百萬)            12,659 稅前淨利(百萬)               397 歸屬母公司業主淨利           308 每股盈餘(元)                0.79 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 3532 | 台勝科 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/06/17 2.發生緣由:依臺灣證券交易所股份有限公司通知辦理 3.財務業務資訊:(IFRS合併) 單位:新台幣佰萬元     最近一月          與去年同期 科目                   (115年5月自結數)        增減% ----------------------------------------------------- 營業收入                     1,218               +24.43% 稅前淨利                       -26               +81.56% 歸屬母公司業主淨利             -26               +81.56% 每股盈餘(元)                 -0.07               +81.56%  單位:新台幣佰萬元     最近一季          與去年同期                          (115年第1季核閱數)        增減% 科目 ----------------------------------------------------- 營業收入                     3,309              +10.87% 稅前淨利                       -82              -127.43% 歸屬母公司業主淨利             -68              -128.61% 每股盈餘(元)                 -0.18              -128.61%  科目             最近四季累計(114年第2季至115年第1季查核數) ----------------------------------------------------- 營業收入(百萬)            12,659 稅前淨利(百萬)               397 歸屬母公司業主淨利           308 每股盈餘(元)                0.79 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3532 | 台勝科 | 1 | 1 | 3 | 5 | 7 | repeated_but_no_breakout | 近 10 日上榜 5 次、近 20 日上榜 7 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3532 | 台勝科 | 44 | 0 | 2634630.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
