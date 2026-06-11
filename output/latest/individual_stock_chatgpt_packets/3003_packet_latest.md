# INDIVIDUAL STOCK CHATGPT PACKET - 3003 健和興

## Metadata
- generated_at: 2026-06-11 22:22:59 Asia/Taipei
- stock_id: 3003
- stock_name: 健和興
- packet_status: standard_180d_window_packet
- latest_price_date: 20260611
- price_rows: 279
- latest_tdcc_date: 20260605
- tdcc_rows: 6
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3003_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3003_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3003_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3003_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3003_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3003_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3003_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3003_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3003_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3003.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3003.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3003.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3003.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3003_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3003_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3003_latest.md?ref=main

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
- risk_control_zh: TDCC 歷史不足
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足

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
- insufficient_tdcc_history

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260611
- open: 64.4
- high: 67
- low: 63.8
- close: 67
- volume: 2701628
- ma5: 63.22
- ema23_primary: 60.77
- distance_to_ema23_pct: 10.25
- ma20: 61.28
- ma60: 55.46
- ma120: 51.91
- return_5d: 7.89
- return_20d: 13.37
- volume_ratio: 1.73
- distance_to_ma20_pct_auxiliary: 9.33
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260512,58.6,60.8,57.5,59.8,2186000,54.91,8.9,55.34,51.6,2.16
20260513,58.6,59.8,57.5,57.9,1259771,55.16,4.96,55.51,51.78,1.25
20260514,58.3,62.5,58.3,61,2863192,55.65,9.62,55.88,52,2.61
20260515,61.6,62,57.7,58.6,1769660,55.89,4.84,56.09,52.17,1.57
20260518,57.7,60,56.3,59,1020092,56.15,5.07,56.3,52.37,0.9
20260519,58.5,59.2,58,58.3,604675,56.33,3.49,56.45,52.55,0.55
20260520,58.3,59.1,57.7,59,709662,56.55,4.33,56.66,52.73,0.64
20260521,59.7,60.8,59.3,60.5,969804,56.88,6.36,56.88,52.92,0.89
20260522,60.9,62.2,59.4,61.9,1655637,57.3,8.03,57.27,53.13,1.49
20260525,62.9,63.5,60.8,61,1738481,57.61,5.89,57.62,53.31,1.51
20260526,61.6,62.8,59.2,62.7,1591485,58.03,8.04,58.06,53.51,1.32
20260527,65.5,66.7,61.8,62.9,3753256,58.44,7.63,58.52,53.72,2.74
20260528,62.9,64.7,61.8,62.2,1965070,58.75,5.87,58.85,53.9,1.37
20260529,63.2,63.7,62,62.7,1079103,59.08,6.12,59.26,54.1,0.74
20260601,63.2,63.4,62,62.1,979968,59.33,4.66,59.59,54.33,0.67
20260602,62.1,62.1,60.3,61.8,1100329,59.54,3.8,59.9,54.53,0.74
20260603,61.8,62.8,61,62.6,836454,59.79,4.69,60.23,54.72,0.56
20260604,62.1,62.1,60.3,61.8,1100329,59.96,3.07,60.53,54.96,0.72
20260605,63,63.4,61.4,62.9,1293492,60.21,4.47,60.89,55.18,0.84
20260611,64.4,67,63.8,67,2701628,60.77,10.25,61.28,55.46,1.73
```

## Latest TDCC Snapshot
- as_of_date: 20260605
- over_400_ratio: 57.21
- over_600_ratio: 54.72
- over_800_ratio: 52.08
- over_1000_ratio: 50.91
- over_400_change_1w: 0.21
- over_800_change_1w: 0.01
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.01,,51.64,,50.57,,0,False,False
20260508,57.48,0.47,51.68,0.04,50.6,0.03,1,True,True
20260515,57.46,-0.02,51.87,0.19,50.73,0.13,2,False,True
20260522,57.65,0.19,51.91,0.04,50.85,0.12,3,True,True
20260529,57,-0.65,52.07,0.16,50.94,0.09,4,False,True
20260605,57.21,0.21,52.08,0.01,50.91,-0.03,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260611 | 3003 | 健和興 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  |  | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_30d |
| 20260611 | 3003 | 健和興 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260611 | 3003 | 健和興 | revenue_breakout_low_response | 營收爆發低反應股 | 17.0 | 11.0 | A_優先追蹤 |  |  |  | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260611 | 3003 | 健和興 | true_breakout | 嚴格突破 | 101.0 |  |  | neckline_challenge |  |  | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260611 | 3003 | 健和興 | 2 | 2 | 2 | 7 | 7 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
