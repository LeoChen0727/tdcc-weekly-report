# INDIVIDUAL STOCK CHATGPT PACKET - 3717 聯嘉投控

## Metadata
- generated_at: 2026-07-01 22:27:49 Asia/Taipei
- stock_id: 3717
- stock_name: 聯嘉投控
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 205
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3717_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3717_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3717_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3717_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3717.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3717.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3717.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3717.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3717_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3717_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3717_latest.md?ref=main

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
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

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
- decision_score_high
- price_structure_not_broken
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
- date: 20260701
- open: 28.2
- high: 30.15
- low: 27.6
- close: 28.95
- volume: 42342000
- ma5: 25.66
- ema23_primary: 23.41
- distance_to_ema23_pct: 23.67
- ma20: 22.79
- ma60: 22.39
- ma120: 20.43
- return_5d: 28.95
- return_20d: 29.24
- volume_ratio: 5.02
- distance_to_ma20_pct_auxiliary: 27.03
- distance_to_high_60_pct: -3.98

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,22.45,23.6,22.45,23.35,3678953,22.47,3.93,22.86,21.57,1.24
20260604,23.5,23.55,22.65,22.85,1973673,22.5,1.56,22.79,21.66,0.71
20260605,22.85,22.85,22.2,22.25,1306331,22.48,-1.02,22.7,21.73,0.52
20260608,20.6,21.45,20.55,21.45,1767604,22.39,-4.21,22.61,21.79,0.72
20260609,21.5,21.5,20.8,21.15,1638773,22.29,-5.11,22.52,21.83,0.68
20260610,21,21.3,20.1,20.2,2731241,22.12,-8.66,22.42,21.85,1.11
20260611,20.2,20.9,20.1,20.3,1765550,21.96,-7.58,22.32,21.87,0.71
20260612,20.6,20.65,20.25,20.25,1077483,21.82,-7.2,22.23,21.89,0.43
20260615,22,22.25,21.4,22.25,3470740,21.86,1.8,22.22,21.95,1.38
20260616,22,23.35,21.65,21.65,4310614,21.84,-0.87,22.18,21.99,1.64
20260617,21.7,23.8,21.7,22.45,19629286,21.89,2.56,22.15,22.03,5.55
20260618,22.8,23.55,22.45,22.55,8578935,21.95,2.75,22.09,22.06,2.31
20260622,23,23.1,21.85,22.2,3417000,21.97,1.06,21.96,22.08,0.93
20260623,22.25,22.3,21.65,22.15,1981281,21.98,0.76,21.93,22.09,0.56
20260624,22,22.45,21.6,22.45,1932954,22.02,1.95,21.93,22.1,0.55
20260625,22.5,22.9,22.1,22.35,3009933,22.05,1.37,21.94,22.1,0.84
20260626,22.2,24.55,22.2,23.6,11385294,22.18,6.41,22.04,22.13,2.88
20260629,25.9,25.95,25.1,25.95,20834636,22.49,15.37,22.21,22.2,4.24
20260630,25.95,27.65,25.45,27.45,31834000,22.91,19.84,22.46,22.28,4.97
20260701,28.2,30.15,27.6,28.95,42342000,23.41,23.67,22.79,22.39,5.02
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 45.36
- over_600_ratio: 39.39
- over_800_ratio: 36.79
- over_1000_ratio: 35.55
- over_400_change_1w: -0.35
- over_800_change_1w: -1.54
- over_1000_change_1w: -0.77
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.77,,39.09,,36.62,,0,False,False
20260508,46.6,-0.17,38.71,-0.38,35.79,-0.83,1,False,False
20260515,46.38,-0.22,38.22,-0.49,35.72,-0.07,0,False,False
20260522,46.89,0.51,39.39,1.17,38.16,2.44,1,True,True
20260529,46.44,-0.45,39.01,-0.38,36.92,-1.24,0,False,False
20260605,45.99,-0.45,38.67,-0.34,36.6,-0.32,0,False,False
20260612,45.27,-0.72,36.88,-1.79,35.18,-1.42,0,False,False
20260618,45.71,0.44,38.33,1.45,36.32,1.14,1,True,True
20260626,45.36,-0.35,36.79,-1.54,35.55,-0.77,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3717 | 聯嘉投控 | true_breakout | 嚴格突破 | 94.0 |  |  | platform_breakout |  |  | continued_overheated | 符合條款第四條第XX款：12 事實發生日：115/06/30 1.召開法人說明會之日期：115/06/30 2.召開法人說明會之時間：14 時 30 分  3.召開法人說明會之地點：台北巿新生南路一段50號3樓 4.法人說明會擇要訊息：德信綜合證券舉辦之法人說明會，向投資人說明財務成果及本年度營運概況暨業務相關資訊。 5.其他應敘明事項：完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表查閱。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3717 | 聯嘉投控 | 5 | 3 | 5 | 7 | 14 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
