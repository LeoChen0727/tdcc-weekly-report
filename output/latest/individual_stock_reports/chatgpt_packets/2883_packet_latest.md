# INDIVIDUAL STOCK CHATGPT PACKET - 2883 凱基金

## Metadata
- generated_at: 2026-08-01 15:53:22 Asia/Taipei
- stock_id: 2883
- stock_name: 凱基金
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2883_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2883_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2883.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2883.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2883.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2883.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2883_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2883_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2883_latest.md?ref=main

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
- date: 20260730
- open: 29.25
- high: 29.25
- low: 28.35
- close: 28.95
- volume: 43927116
- ma5: 29.81
- ema23_primary: 29.52
- distance_to_ema23_pct: -1.92
- ma20: 29.79
- ma60: 26.9
- ma120: 23.52
- return_5d: -6.16
- return_20d: 2.3
- volume_ratio: 0.81
- distance_to_ma20_pct_auxiliary: -2.82
- distance_to_high_60_pct: -7.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,28.2,28.5,27.75,27.9,70576026,27.91,-0.05,28.94,24.1,0.45
20260703,27.6,28.55,27.6,28.45,59279024,27.96,1.76,29,24.22,0.45
20260706,28.65,29.1,28.55,29,40813724,28.04,3.41,29.07,24.34,0.34
20260707,28.75,30.9,28.75,30.1,126248707,28.22,6.68,29.23,24.49,1.13
20260708,30.9,31.2,30.4,30.7,73026098,28.42,8.01,29.32,24.65,0.72
20260709,30.7,30.95,29.75,30.05,42202807,28.56,5.22,29.41,24.81,0.45
20260713,30.1,30.65,29.7,29.8,36468752,28.66,3.97,29.51,24.96,0.42
20260714,30.1,30.1,28.9,29.5,49240296,28.73,2.67,29.61,25.1,0.58
20260715,30.2,31,30.05,30.15,53145417,28.85,4.51,29.68,25.25,0.64
20260716,30.1,30.55,29.7,30.55,45149452,28.99,5.38,29.72,25.41,0.57
20260717,30,30.45,29.7,30,52680322,29.08,3.18,29.71,25.57,0.71
20260720,30.45,30.6,29.55,29.55,70442629,29.12,1.49,29.65,25.71,0.99
20260721,29.8,30.2,29.5,29.7,40555983,29.16,1.84,29.62,25.87,0.59
20260722,29.7,30.8,29.7,30.45,59155620,29.27,4.03,29.64,26.04,0.88
20260723,30.8,31.3,30.5,30.85,43024593,29.4,4.92,29.69,26.21,0.65
20260724,30.45,30.95,30.4,30.65,37493589,29.51,3.88,29.7,26.37,0.57
20260727,30.95,30.95,30.5,30.7,29839072,29.61,3.69,29.74,26.52,0.47
20260728,30.5,30.55,29.3,29.6,49832372,29.61,-0.02,29.73,26.66,0.82
20260729,29.65,29.95,28.5,29.15,58342967,29.57,-1.41,29.76,26.78,1.04
20260730,29.25,29.25,28.35,28.95,43927116,29.52,-1.92,29.79,26.9,0.81
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 68.08
- over_600_ratio: 66.35
- over_800_ratio: 65.17
- over_1000_ratio: 64.22
- over_400_change_1w: 0.01
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,66.62,0.04,63.56,0.08,62.69,0.08,2,True,True
20260522,66.49,-0.13,63.42,-0.14,62.55,-0.14,0,False,False
20260529,66.61,0.12,63.55,0.13,62.65,0.1,1,True,True
20260605,67.15,0.54,64.23,0.68,63.36,0.71,2,True,True
20260612,67.59,0.44,64.75,0.52,63.87,0.51,3,True,True
20260618,67.69,0.1,64.86,0.11,63.93,0.06,4,True,True
20260626,67.59,-0.1,64.72,-0.14,63.78,-0.15,0,False,False
20260703,67.26,-0.33,64.28,-0.44,63.32,-0.46,0,False,False
20260709,67.7,0.44,64.75,0.47,63.82,0.5,1,True,True
20260717,67.79,0.09,64.81,0.06,63.84,0.02,2,True,True
20260724,68.07,0.28,65.15,0.34,64.18,0.34,3,True,True
20260731,68.08,0.01,65.17,0.02,64.22,0.04,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2883 | 凱基金 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  | call_strong_inflow | stale_signal | 1.事實發生日:115/07/14 2.公司名稱:凱基金融控股股份有限公司(原名稱：中華開發金融控股股份有限公司) 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司暨主要子公司115年6月份自結合併盈餘 6.因應措施:無 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):                                  合併稅後(億元) -------------------------------------------------------------------------- 　                     6月份                 累計 1 至 6 月份 -------------------------------------------------------------------------- 　           總損益   母公司  非控制   總損益   母公司  非控制  稅後每股 　　　　               業主    權益              業主    權益    盈餘(元) -------------------------------------------------------------------------- 凱基金控      61.14    61.10   0.04    284.48   284.40    0.08    1.64 凱基人壽      15.16    15.16   0.00     92.03    92.03    0.00    1.76 凱基銀行       6.86     6.86   0.00     42.76    42.76    0.00    0.91 中華開發資本  -0.88    -0.89   0.01      7.51     7.49    0.02    0.37 凱基證券      50.34    50.30   0.04    179.42   179.36    0.06    9.87 上述資料均係公司自結數。 註1：凱基人壽累計6月未適用外匯價格變動準備金之EPS(元)：2.63 註2：金控累計6月淨利加計透過其他綜合損益按公允價值衡量之股票累計處分利益 為677.75億元。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2883 | 凱基金 | 16 | 6 | 5 | 10 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2883 | 凱基金 | 26 | 0 | 3272430.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
