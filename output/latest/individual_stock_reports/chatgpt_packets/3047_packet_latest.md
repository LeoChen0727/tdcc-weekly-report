# INDIVIDUAL STOCK CHATGPT PACKET - 3047 訊舟

## Metadata
- generated_at: 2026-07-06 22:27:06 Asia/Taipei
- stock_id: 3047
- stock_name: 訊舟
- packet_status: standard_180d_window_packet
- latest_price_date: 20260706
- price_rows: 298
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3047_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3047_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3047_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3047_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3047_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3047_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3047_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3047_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3047_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3047_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3047_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3047_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3047.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3047.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3047.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3047.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3047_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3047_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3047_latest.md?ref=main

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
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
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
- date: 20260706
- open: 16.8
- high: 17.5
- low: 16.5
- close: 16.8
- volume: 4718000
- ma5: 15.93
- ema23_primary: 15.76
- distance_to_ema23_pct: 6.63
- ma20: 15.8
- ma60: 15.38
- ma120: 16.43
- return_5d: 12.37
- return_20d: 4.02
- volume_ratio: 2.1
- distance_to_ma20_pct_auxiliary: 6.35
- distance_to_high_60_pct: -4.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260608,14.75,15.45,14.6,15.35,1930817,15.42,-0.49,15.15,15.48,0.9
20260609,15.35,15.7,15.15,15.6,1041032,15.44,1.04,15.2,15.47,0.49
20260610,15.5,16.9,15.45,15.6,3745684,15.45,0.95,15.27,15.47,1.65
20260611,15.6,15.85,15.35,15.75,1180422,15.48,1.76,15.34,15.46,0.52
20260612,15.9,16.2,15.7,15.8,1147631,15.5,1.91,15.42,15.44,0.5
20260615,16,16.05,15.75,15.85,923434,15.53,2.04,15.48,15.43,0.41
20260616,16,16.1,15.4,15.4,981423,15.52,-0.79,15.55,15.41,0.43
20260617,15.45,16.9,15.4,16.9,5800135,15.64,8.08,15.68,15.41,2.29
20260618,17,17.25,16.3,16.65,8132538,15.72,5.91,15.78,15.42,2.81
20260622,16.65,16.65,16.2,16.2,3029188,15.76,2.78,15.82,15.43,1.06
20260623,16.3,16.45,15.8,15.9,1713380,15.77,0.81,15.84,15.42,0.61
20260624,15.8,16.05,15.6,15.85,1721249,15.78,0.45,15.88,15.42,0.61
20260625,16,16,15.5,15.6,1194646,15.76,-1.04,15.91,15.4,0.42
20260626,15.45,15.45,14.9,14.9,1909784,15.69,-5.05,15.92,15.38,0.68
20260629,14.9,15.3,14.7,14.95,917856,15.63,-4.35,15.91,15.37,0.33
20260630,15.2,15.7,15.05,15.65,1256000,15.63,0.11,15.92,15.36,0.46
20260701,15.65,15.75,15.3,15.35,1013000,15.61,-1.66,15.84,15.36,0.41
20260702,15.35,15.75,15.2,15.75,920000,15.62,0.83,15.78,15.37,0.42
20260703,15.75,16.4,15.6,16.1,1687548,15.66,2.81,15.77,15.37,0.8
20260706,16.8,17.5,16.5,16.8,4718000,15.76,6.63,15.8,15.38,2.1
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 19.82
- over_600_ratio: 16.9
- over_800_ratio: 15.77
- over_1000_ratio: 15.02
- over_400_change_1w: -0.4
- over_800_change_1w: 0.22
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,18.64,,15.44,,15.04,,0,False,False
20260508,18.96,0.32,15.57,0.13,15.15,0.11,1,True,True
20260515,19.31,0.35,15.65,0.08,15.3,0.15,2,False,True
20260522,19.89,0.58,15.38,-0.27,15.38,0.08,3,False,True
20260529,20.6,0.71,16.3,0.92,15.88,0.5,4,True,True
20260605,20.75,0.15,15.17,-1.13,15.17,-0.71,5,False,False
20260612,20.57,-0.18,15.18,0.01,15.18,0.01,6,False,True
20260618,21.01,0.44,16.71,1.53,16.71,1.53,7,True,True
20260626,20.22,-0.79,15.55,-1.16,15.17,-1.54,0,False,False
20260703,19.82,-0.4,15.77,0.22,15.02,-0.15,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 3047 | 訊舟 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | continued_2_3d | 1.發生變動日期:115/06/16 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名: 獨立董事:曹忠明 獨立董事:駱金生 獨立董事:林宇亮 4.舊任者簡歷: 獨立董事:曹忠明   曹忠明會計師事務所負責人 獨立董事:駱金生   鎮江月曆(股)公司監察人 獨立董事:林宇亮   恆美化工(股)公司董事兼副總經理、亞洲光學(股)公司董事 5.新任者姓名: 獨立董事:曹忠明 獨立董事:駱金生 獨立董事:林宇亮 6.新任者簡歷: 獨立董事:曹忠明   曹忠明會計師事務所負責人 獨立董事:駱金生   鎮江月曆(股)公司監察人 獨立董事:林宇亮   恆美化工(股)公司董事兼副總經理、亞洲光學(股)公司董事 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿全面改選 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/30~115/06/13 10.新任生效日期:115/06/16 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 3047 | 訊舟 | 2 | 1 | 2 | 3 | 10 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
