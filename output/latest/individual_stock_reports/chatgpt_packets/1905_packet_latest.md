# INDIVIDUAL STOCK CHATGPT PACKET - 1905 華紙

## Metadata
- generated_at: 2026-06-21 22:22:45 Asia/Taipei
- stock_id: 1905
- stock_name: 華紙
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1905_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1905_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1905_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1905_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1905_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1905_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1905_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1905_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1905_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1905_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1905_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1905_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1905.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1905.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1905.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1905.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1905_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1905_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1905_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
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
- model_recommended
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260618
- open: 15.95
- high: 17.1
- low: 15.4
- close: 17.1
- volume: 44217266
- ma5: 14.52
- ema23_primary: 13.36
- distance_to_ema23_pct: 27.95
- ma20: 13
- ma60: 13.41
- ma120: 12.69
- return_5d: 34.65
- return_20d: 41.32
- volume_ratio: 3.83
- distance_to_ma20_pct_auxiliary: 31.51
- distance_to_high_60_pct: -7.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,12.15,12.15,11.9,12.1,2769456,12.59,-3.88,12.52,13.06,0.69
20260525,12.15,12.25,11.75,12.25,5981013,12.56,-2.47,12.45,13.06,1.51
20260526,12.35,12.4,11.9,12,3701519,12.51,-4.11,12.38,13.05,1.07
20260527,12.05,12.05,11.8,11.85,3142575,12.46,-4.89,12.3,13.04,0.91
20260528,11.9,12.15,11.8,11.95,4864199,12.42,-3.76,12.24,13.03,1.36
20260529,11.95,12.15,11.9,11.95,3276333,12.38,-3.45,12.19,13.03,0.91
20260601,11.95,12.2,11.8,12.15,4198922,12.36,-1.69,12.16,13.04,1.17
20260602,12.15,12.25,12,12.25,3353052,12.35,-0.81,12.13,13.04,0.92
20260603,12.25,12.75,12.15,12.75,8576386,12.38,2.96,12.14,13.05,2.17
20260604,13,14,12.75,14,41543307,12.52,11.84,12.21,13.09,7.11
20260605,13.4,13.55,12.65,13.05,17669865,12.56,3.88,12.23,13.11,2.68
20260608,12.25,12.95,12.1,12.7,6515269,12.57,1.01,12.25,13.12,0.96
20260609,12.75,13.25,12.35,12.8,8536471,12.59,1.65,12.29,13.14,1.23
20260610,12.95,13.4,12.9,12.95,7744941,12.62,2.6,12.33,13.17,1.08
20260611,13.15,13.15,12.6,12.7,4993710,12.63,0.56,12.36,13.19,0.69
20260612,12.9,13.05,12.75,12.9,3345268,12.65,1.97,12.4,13.21,0.47
20260615,13.05,13.15,12.8,12.9,4332978,12.67,1.8,12.45,13.22,0.6
20260616,13,14.15,12.75,14.15,14957118,12.8,10.59,12.56,13.27,1.93
20260617,15.55,15.55,15.55,15.55,37075531,13.02,19.39,12.75,13.33,3.91
20260618,15.95,17.1,15.4,17.1,44217266,13.36,27.95,13,13.41,3.83
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 71.79
- over_600_ratio: 70.83
- over_800_ratio: 70.19
- over_1000_ratio: 69.55
- over_400_change_1w: 0.62
- over_800_change_1w: 0.8
- over_1000_change_1w: 0.71
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.23,,70.35,,69.61,,0,False,False
20260508,72.03,-0.2,70.2,-0.15,69.42,-0.19,0,False,False
20260515,71.81,-0.22,69.92,-0.28,69.11,-0.31,0,False,False
20260522,71.48,-0.33,69.71,-0.21,69.13,0.02,1,False,True
20260529,71.39,-0.09,69.77,0.06,68.99,-0.14,2,False,True
20260605,71.5,0.11,69.51,-0.26,68.95,-0.04,3,False,False
20260612,71.17,-0.33,69.39,-0.12,68.84,-0.11,0,False,False
20260618,71.79,0.62,70.19,0.8,69.55,0.71,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1905 | 華紙 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  | call_inflow | continued_overheated | 1.股東常會日期:115/06/16 2.重要決議事項一、盈餘分配或盈虧撥補:   承認本公司2025年度虧損撥補案。 3.重要決議事項二、章程修訂:無 4.重要決議事項三、營業報告書及財務報表:   承認本公司2025年度決算表冊。 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:無 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1905 | 華紙 | 3 | 3 | 3 | 7 | 14 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1905 | 華紙 | 3 | 0 | 1571170.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
