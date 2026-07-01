# INDIVIDUAL STOCK CHATGPT PACKET - 3055 蔚華科

## Metadata
- generated_at: 2026-07-01 22:27:31 Asia/Taipei
- stock_id: 3055
- stock_name: 蔚華科
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3055_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3055_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3055_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3055_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3055_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3055_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3055_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3055_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3055_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3055_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3055_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3055_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3055.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3055.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3055.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3055.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3055_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3055_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3055_latest.md?ref=main

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
- open: 127.5
- high: 127.5
- low: 126
- close: 127.5
- volume: 4518000
- ma5: 109.4
- ema23_primary: 99.51
- distance_to_ema23_pct: 28.13
- ma20: 94.98
- ma60: 91.16
- ma120: 78.96
- return_5d: 27.63
- return_20d: 25
- volume_ratio: 2.02
- distance_to_ma20_pct_auxiliary: 34.24
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,102.5,109.5,100.5,100.5,2118158,102.59,-2.03,108.41,79.73,0.37
20260604,100,105.5,99.5,103.5,1590011,102.66,0.82,109.23,80.47,0.28
20260605,102.5,103.5,98,99.5,1449380,102.4,-2.83,109.65,81.15,0.28
20260608,89.6,92.9,89.6,91,1490825,101.45,-10.3,109.2,81.66,0.29
20260609,91,91,85.5,87.8,3100070,100.31,-12.47,108.09,82.14,0.62
20260610,87.8,90.7,81.6,82,2226895,98.79,-16.99,106.52,82.55,0.49
20260611,80.2,82.9,78.3,79.5,1649060,97.18,-18.19,105.19,82.89,0.37
20260612,82.7,82.8,79.9,79.9,1014785,95.74,-16.54,104.03,83.23,0.24
20260615,84.6,85.4,82.8,83.1,1276941,94.69,-12.24,102.54,83.61,0.32
20260616,85.2,87.4,83.2,85.1,1485518,93.89,-9.36,100.59,84.04,0.45
20260617,84.9,87.5,83.2,86.8,1068061,93.3,-6.96,99.33,84.49,0.36
20260618,89.8,95,86.8,91.1,2907958,93.11,-2.16,98.06,85.04,1.06
20260622,94.5,97.2,91.5,92,1818799,93.02,-1.1,96.77,85.62,0.7
20260623,92.6,92.6,88.1,90.9,1294045,92.84,-2.09,95.41,86.12,0.55
20260624,89.1,99.9,88.5,99.9,2932613,93.43,6.92,94.45,86.82,1.29
20260625,104,104.5,95.4,102,6103663,94.15,8.34,93.93,87.55,2.58
20260626,99,103.5,95.3,96,2369515,94.3,1.8,93.45,88.2,1.05
20260629,96,105.5,93.6,105.5,2857928,95.23,10.78,93.33,89.03,1.24
20260630,116,116,116,116,1433000,96.96,19.63,93.7,89.99,0.65
20260701,127.5,127.5,126,127.5,4518000,99.51,28.13,94.98,91.16,2.02
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 66.1
- over_600_ratio: 63.36
- over_800_ratio: 62.1
- over_1000_ratio: 59.82
- over_400_change_1w: 0.26
- over_800_change_1w: 0.49
- over_1000_change_1w: -0.23
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.82,,64.37,,62.19,,0,False,False
20260508,69.1,0.28,64.78,0.41,63.25,1.06,1,True,True
20260515,68.78,-0.32,62.73,-2.05,61.33,-1.92,0,False,False
20260522,68.31,-0.47,64.26,1.53,60.32,-1.01,1,False,True
20260529,68.77,0.46,63.73,-0.53,59.87,-0.45,2,False,False
20260605,67.5,-1.27,61.22,-2.51,60.51,0.64,3,False,True
20260612,66.79,-0.71,61.85,0.63,59.52,-0.99,4,False,True
20260618,65.84,-0.95,61.61,-0.24,60.05,0.53,5,False,True
20260626,66.1,0.26,62.1,0.49,59.82,-0.23,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3055 | 蔚華科 | true_breakout | 嚴格突破 | 94.0 |  |  | breakout_confirmed |  | call_inflow | first_seen | 1. 董事會決議日期：115/06/24 2. 股利所屬年(季)度：114年 年度 3. 股利所屬期間：114/01/01 至 114/12/31 4. 股東配發內容： 　(1)盈餘分配之現金股利(元/股)：0 　(2)法定盈餘公積發放之現金(元/股)：0 　(3)資本公積發放之現金(元/股)：0.50000000 　(4)股東配發之現金(股利)總金額(元)：56,543,459 　(5)盈餘轉增資配股(元/股)：0 　(6)法定盈餘公積轉增資配股(元/股)：0 　(7)資本公積轉增資配股(元/股)：0 　(8)股東配股總股數(股)：0 5. 其他應敘明事項： 115/06/24股東常會議決通過以法定盈餘公積 新台幣297,623,847元彌補虧損後，同日董事會 議決通過自資本公積之股票發行溢價項下提撥 現&#12198;新台幣56,543,459元配發予股東。 6. 普通股每股面額欄位：新台幣10.0000元；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3055 | 蔚華科 | 1 | 1 | 4 | 7 | 13 | first_seen | 首次上榜或資料有限，需後續確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3055 | 蔚華科 | 7 | 0 | 1298800.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
