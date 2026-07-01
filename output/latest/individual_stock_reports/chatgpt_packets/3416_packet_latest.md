# INDIVIDUAL STOCK CHATGPT PACKET - 3416 融程電

## Metadata
- generated_at: 2026-07-01 22:27:40 Asia/Taipei
- stock_id: 3416
- stock_name: 融程電
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3416_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3416_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3416_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3416_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3416_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3416_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3416_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3416_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3416_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3416_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3416_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3416_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3416.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3416.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3416.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3416.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3416_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3416_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3416_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260701
- open: 179.5
- high: 192
- low: 177.5
- close: 179.5
- volume: 1490000
- ma5: 171.4
- ema23_primary: 173.71
- distance_to_ema23_pct: 3.33
- ma20: 174.62
- ma60: 168.35
- ma120: 158.23
- return_5d: 4.97
- return_20d: -1.64
- volume_ratio: 3.58
- distance_to_ma20_pct_auxiliary: 2.79
- distance_to_high_60_pct: -8.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,183.5,185.5,181,182.5,326396,174.6,4.52,175.88,160.02,0.37
20260604,182.5,182.5,178.5,180,305966,175.05,2.83,176.3,160.67,0.38
20260605,180,181,176.5,181,327531,175.55,3.11,176.57,161.32,0.44
20260608,165,174.5,164.5,174.5,507919,175.46,-0.55,176.72,161.78,0.7
20260609,175,180.5,174.5,176.5,361621,175.55,0.54,177.03,162.28,0.51
20260610,173.5,178.5,169.5,174.5,511680,175.46,-0.55,177.4,162.72,0.72
20260611,173.5,173.5,165,171,438421,175.09,-2.34,177.53,163.07,0.61
20260612,173.5,176,173,174,225180,175,-0.57,178.07,163.43,0.32
20260615,176.5,178.5,175,177.5,249162,175.21,1.31,178.53,163.82,0.37
20260616,178,178,173.5,173.5,173404,175.06,-0.89,179.03,164.21,0.26
20260617,174,175,172.5,174.5,126997,175.02,-0.3,179.43,164.61,0.19
20260618,175,178,175,176,229907,175.1,0.51,179.55,165.03,0.37
20260622,178,179,176,177.5,267209,175.3,1.26,179.28,165.48,0.49
20260623,179,179,171,171.5,337720,174.98,-1.99,178.32,165.81,0.78
20260624,169,172,168.5,171,294543,174.65,-2.09,177.47,166.19,0.73
20260625,173.5,173.5,169,170,306921,174.26,-2.45,176.72,166.51,0.82
20260626,169,172,163.5,163.5,463562,173.37,-5.69,175.95,166.8,1.31
20260629,165.5,169,164.5,166.5,352891,172.79,-3.64,175.1,167.19,1.03
20260630,165,177.5,161.5,177.5,1017000,173.19,2.49,174.78,167.75,2.77
20260701,179.5,192,177.5,179.5,1490000,173.71,3.33,174.62,168.35,3.58
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 56
- over_600_ratio: 55.33
- over_800_ratio: 53.65
- over_1000_ratio: 51.39
- over_400_change_1w: -0.46
- over_800_change_1w: -0.43
- over_1000_change_1w: -0.43
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.28,,53.89,,51.63,,0,False,False
20260508,56.34,0.06,54.87,0.98,51.58,-0.05,1,False,True
20260515,56.1,-0.24,53.73,-1.14,51.47,-0.11,0,False,False
20260522,56.18,0.08,53.86,0.13,51.6,0.13,1,True,True
20260529,56.05,-0.13,53.85,-0.01,51.59,-0.01,0,False,False
20260605,56.13,0.08,53.87,0.02,51.61,0.02,1,True,True
20260612,55.86,-0.27,53.63,-0.24,51.37,-0.24,0,False,False
20260618,56.46,0.6,54.08,0.45,51.82,0.45,1,True,True
20260626,56,-0.46,53.65,-0.43,51.39,-0.43,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3416 | 融程電 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | call_strong_inflow | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |
| 20260701 | 3416 | 融程電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_strong_inflow | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260701 | 3416 | 融程電 | revenue_breakout_low_response | 營收爆發低反應股 | 11.0 | 38.0 | D_降級_TDCC轉弱 |  |  | call_strong_inflow | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260701 | 3416 | 融程電 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_strong_inflow | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3416 | 融程電 | 2 | 2 | 2 | 2 | 2 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3416 | 融程電 | 14 | 0 | 5326460.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
