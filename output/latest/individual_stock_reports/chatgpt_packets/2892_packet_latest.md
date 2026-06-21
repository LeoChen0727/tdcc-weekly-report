# INDIVIDUAL STOCK CHATGPT PACKET - 2892 第一金

## Metadata
- generated_at: 2026-06-21 22:23:11 Asia/Taipei
- stock_id: 2892
- stock_name: 第一金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2892_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2892_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2892_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2892_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2892_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2892_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2892_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2892_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2892_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2892_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2892_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2892_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2892.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2892.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2892.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2892.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2892_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2892_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2892_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260618
- open: 32.5
- high: 32.8
- low: 32.25
- close: 32.6
- volume: 75198702
- ma5: 31.84
- ema23_primary: 30.02
- distance_to_ema23_pct: 8.6
- ma20: 29.45
- ma60: 28.94
- ma120: 29.13
- return_5d: 6.36
- return_20d: 17.69
- volume_ratio: 1.17
- distance_to_ma20_pct_auxiliary: 10.71
- distance_to_high_60_pct: -0.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,27.8,27.8,27.4,27.55,84956255,28.66,-3.86,28.72,28.81,1.8
20260525,27.6,27.6,27.2,27.6,79808642,28.57,-3.39,28.69,28.77,1.59
20260526,27.55,27.8,27.5,27.7,47398325,28.5,-2.8,28.66,28.73,0.93
20260527,27.7,27.8,27.55,27.6,33694772,28.42,-2.89,28.62,28.7,0.65
20260528,27.6,27.65,27.25,27.25,47996477,28.32,-3.79,28.55,28.66,0.9
20260529,27.3,27.5,27.2,27.45,109953818,28.25,-2.84,28.48,28.62,2.01
20260601,27.45,27.85,27.3,27.75,52244946,28.21,-1.63,28.46,28.6,0.95
20260602,27.75,28.2,27.7,28.15,57901717,28.2,-0.19,28.45,28.59,1.02
20260603,28.4,29.3,28.1,29,81559026,28.27,2.58,28.46,28.58,1.39
20260604,29,29.65,28.85,29.55,89347433,28.38,4.13,28.48,28.59,1.48
20260605,29.5,29.55,28.95,29.3,57303236,28.45,2.97,28.47,28.59,0.94
20260608,28.7,29.15,28.45,29.1,50961160,28.51,2.08,28.45,28.59,0.82
20260609,29.1,30.55,29.1,30.5,99331453,28.67,6.37,28.5,28.62,1.54
20260610,30.4,30.95,30.2,30.55,68192460,28.83,5.96,28.55,28.65,1.03
20260611,30.55,30.75,29.95,30.65,46641122,28.98,5.75,28.61,28.68,0.69
20260612,30.7,31.35,30.65,31,48818443,29.15,6.35,28.7,28.71,0.71
20260615,31.35,31.65,31.05,31.3,39236972,29.33,6.72,28.82,28.75,0.57
20260616,31.3,31.8,31.25,31.8,50858769,29.54,7.67,28.96,28.8,0.72
20260617,31.8,32.75,31.7,32.5,65779573,29.78,9.12,29.2,28.87,1.01
20260618,32.5,32.8,32.25,32.6,75198702,30.02,8.6,29.45,28.94,1.17
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 70.73
- over_600_ratio: 68.83
- over_800_ratio: 67.65
- over_1000_ratio: 66.78
- over_400_change_1w: 0.38
- over_800_change_1w: 0.41
- over_1000_change_1w: 0.41
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,69.93,,66.8,,65.87,,0,False,False
20260508,70.22,0.29,67.09,0.29,66.17,0.3,1,True,True
20260515,70.52,0.3,67.41,0.32,66.52,0.35,2,True,True
20260522,69.55,-0.97,66.35,-1.06,65.48,-1.04,0,False,False
20260529,68.95,-0.6,65.73,-0.62,64.85,-0.63,0,False,False
20260605,69.48,0.53,66.29,0.56,65.42,0.57,1,True,True
20260612,70.35,0.87,67.24,0.95,66.37,0.95,2,True,True
20260618,70.73,0.38,67.65,0.41,66.78,0.41,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2892 | 第一金 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | repeated_but_no_breakout | 1.股東常會日期:115/06/18 2.重要決議事項一、盈餘分配或盈虧撥補:  通過本公司114年度盈餘分派。 3.重要決議事項二、章程修訂:  無。 4.重要決議事項三、營業報告書及財務報表:  通過本公司114年度營業報告書及合併財務報告。 5.重要決議事項四、董監事選舉:  無。 6.重要決議事項五、其他事項:  通過修正「第一金融控股股份有限公司取得或處分資產處理程序」。 7.其他應敘明事項:  無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2892 | 第一金 | 17 | 1 | 5 | 10 | 17 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 17 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2892 | 第一金 | 6 | 0 | 1331890.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
