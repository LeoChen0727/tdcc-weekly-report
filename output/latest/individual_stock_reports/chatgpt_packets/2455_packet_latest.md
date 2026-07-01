# INDIVIDUAL STOCK CHATGPT PACKET - 2455 全新

## Metadata
- generated_at: 2026-07-01 22:27:14 Asia/Taipei
- stock_id: 2455
- stock_name: 全新
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 295
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2455_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2455_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2455_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2455_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2455.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2455.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2455.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2455.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2455_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2455_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2455_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
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
- date: 20260701
- open: 359.5
- high: 365
- low: 357
- close: 358.5
- volume: 1005000
- ma5: 355.6
- ema23_primary: 376.88
- distance_to_ema23_pct: -4.88
- ma20: 379.9
- ma60: 362.03
- ma120: 279.11
- return_5d: -9.7
- return_20d: -10.15
- volume_ratio: 0.14
- distance_to_ma20_pct_auxiliary: -5.63
- distance_to_high_60_pct: -22.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,413.5,422,413.5,414,1545220,386.27,7.18,390.75,317.7,0.23
20260604,405,405,395,402,962838,387.58,3.72,393.75,321.14,0.14
20260605,390,399,374,399,2141199,388.54,2.69,396.85,324.43,0.32
20260608,359.5,360.5,359.5,359.5,1699795,386.12,-6.89,396.82,326.73,0.26
20260609,373,395,360,395,1982555,386.86,2.1,397.82,329.6,0.3
20260610,365.5,382,355.5,355.5,14717488,384.24,-7.48,396.9,331.57,2.04
20260611,343,350,320,320,13723008,378.89,-15.54,394.98,333.08,1.77
20260612,338,352,326.5,352,12419013,376.65,-6.54,394.65,335.35,1.5
20260615,371,373.5,355,369,15918921,376.01,-1.86,393.75,337.71,1.79
20260616,387,405.5,387,405.5,17713592,378.47,7.14,394.88,340.68,1.83
20260617,399,434,399,428,23916300,382.6,11.87,396.25,343.98,2.52
20260618,421.5,447.5,412,416,25326353,385.38,7.95,397.73,347.23,2.62
20260622,412,412,400.5,409.5,2607383,387.39,5.71,396.95,350.01,0.29
20260623,408,408,390,398,1610653,388.27,2.5,394.65,352.2,0.2
20260624,385,397,368,397,1802349,389,2.06,393.32,354.28,0.24
20260625,400,400,384.5,388.5,1095463,388.96,-0.12,391.82,356.25,0.15
20260626,382.5,382.5,347.5,348,2529904,385.55,-9.74,389.65,357.49,0.34
20260629,339,348,333,336,1920109,381.42,-11.91,385.35,358.98,0.26
20260630,343.5,360,340.5,347,2640000,378.55,-8.33,381.93,360.38,0.36
20260701,359.5,365,357,358.5,1005000,376.88,-4.88,379.9,362.03,0.14
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 52.09
- over_600_ratio: 45.95
- over_800_ratio: 40.71
- over_1000_ratio: 38.83
- over_400_change_1w: -0.28
- over_800_change_1w: 0.31
- over_1000_change_1w: 0.25
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.25,,34.57,,31.64,,0,False,False
20260508,51.22,2.97,38.83,4.26,36.47,4.83,1,True,True
20260515,51.8,0.58,39.41,0.58,36.11,-0.36,2,False,True
20260522,49.01,-2.79,37.33,-2.08,33.55,-2.56,0,False,False
20260529,50.37,1.36,38.57,1.24,35.26,1.71,1,True,True
20260605,50.92,0.55,38.46,-0.11,35.56,0.3,2,False,True
20260612,48.72,-2.2,36.52,-1.94,33.57,-1.99,0,False,False
20260618,52.37,3.65,40.4,3.88,38.58,5.01,1,True,True
20260626,52.09,-0.28,40.71,0.31,38.83,0.25,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2455 | 全新 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/06/16 2.發生緣由:依臺灣證券交易所股份有限公司通知辦理。 3.財務業務資訊:           最近一月  與去年同期   最近一季   與去年同期    最近四季累計 科目     115年04月    增減(%)   115年第1季     增減%       114年第2季                                                           至115年第1季                 (自結數)               (核閱數)           (核閱/查核數) --------------------------------------------------------------------------- 營業收入   318.60     37.75%       959.31     20.87%         3545.79 (百萬) 稅前淨利    89.68    100.63%       243.60     23.89%          714.33 (百萬) 本期淨利    71.74    100.62%       195.09     24.03%          585.74 (百萬) 每股盈餘     0.39    105.26%         1.06     24.71%            3.18 (元) 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2455 | 全新 | 14 | 7 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2455 | 全新 | 38 | 0 | 255480.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
