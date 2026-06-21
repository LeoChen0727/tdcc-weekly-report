# INDIVIDUAL STOCK CHATGPT PACKET - 8431 匯鑽科

## Metadata
- generated_at: 2026-06-21 22:24:48 Asia/Taipei
- stock_id: 8431
- stock_name: 匯鑽科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 152
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8431_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8431_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8431_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8431_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8431_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8431_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8431_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8431_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8431_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8431_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8431_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8431_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8431.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8431.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8431.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8431.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8431_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8431_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8431_latest.md?ref=main

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
- open: 57.7
- high: 58.2
- low: 56.1
- close: 57.6
- volume: 1024000
- ma5: 53.62
- ema23_primary: 55.07
- distance_to_ema23_pct: 4.6
- ma20: 54.59
- ma60: 60.1
- ma120: 63.31
- return_5d: 21.01
- return_20d: 0
- volume_ratio: 2.15
- distance_to_ma20_pct_auxiliary: 5.52
- distance_to_high_60_pct: -25.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,57.8,62,57.8,60.8,61000,61.05,-0.41,60.95,64.43,0.06
20260525,61.2,61.9,59.1,59.8,60000,60.94,-1.88,60.63,64.34,0.07
20260526,60,60.5,58.5,59.2,59000,60.8,-2.63,60.45,64.15,0.07
20260527,59.6,59.8,57.1,57.3,58000,60.51,-5.3,60.17,63.92,0.07
20260528,57.3,58.1,55.6,55.9,57000,60.12,-7.03,59.74,63.68,0.09
20260529,56.2,56.8,55.5,55.9,56000,59.77,-6.48,59.38,63.49,0.09
20260601,56.1,56.6,55.3,55.8,56000,59.44,-6.13,59.03,63.33,0.1
20260602,56,56,53.6,53.9,54,58.98,-8.61,58.59,63.16,0
20260603,54.6,57.8,53.6,57.2,56000,58.83,-2.77,58.34,62.99,0.13
20260604,57.2,57.2,55.8,55.8,56000,58.58,-4.74,58.03,62.91,0.14
20260605,56,56,54,54.3,55000,58.22,-6.74,57.72,62.74,0.16
20260608,48.95,51.5,48.9,51.3,689000,57.65,-11.01,57.23,62.42,1.97
20260609,51.8,52.8,50.8,50.8,547000,57.07,-10.99,56.72,62.09,1.56
20260610,49.95,51,48.05,48.05,731000,56.32,-14.69,56.17,61.76,2.13
20260611,48.05,48.4,46.25,47.6,673000,55.6,-14.38,55.67,61.44,2.09
20260612,48.25,49.5,48.1,48.8,377000,55.03,-11.32,55.19,61.05,1.28
20260615,49.55,49.65,48.85,49,364000,54.53,-10.14,54.74,60.65,1.23
20260616,52.8,53.9,52.5,53.9,412000,54.47,-1.05,54.5,60.36,1.49
20260617,59.2,59.2,55.3,58.8,4123000,54.84,7.23,54.59,60.19,8.99
20260618,57.7,58.2,56.1,57.6,1024000,55.07,4.6,54.59,60.1,2.15
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 24.21
- over_600_ratio: 20.47
- over_800_ratio: 17.24
- over_1000_ratio: 15.4
- over_400_change_1w: 0.82
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,24.43,,17.61,,15.77,,0,False,False
20260508,24.33,-0.1,17.61,0,15.77,0,0,False,False
20260515,24.42,0.09,17.63,0.02,15.79,0.02,1,True,True
20260522,24.34,-0.08,17.63,0,15.79,0,0,False,False
20260529,24.4,0.06,17.62,-0.01,15.78,-0.01,1,False,False
20260605,24.57,0.17,17.62,0,15.78,0,2,False,False
20260612,23.39,-1.18,17.28,-0.34,15.44,-0.34,0,False,False
20260618,24.21,0.82,17.24,-0.04,15.4,-0.04,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 8431 | 匯鑽科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 8431 | 匯鑽科 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
