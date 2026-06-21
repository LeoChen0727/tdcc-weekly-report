# INDIVIDUAL STOCK CHATGPT PACKET - 2603 長榮

## Metadata
- generated_at: 2026-06-21 22:23:05 Asia/Taipei
- stock_id: 2603
- stock_name: 長榮
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2603_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2603_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2603_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2603_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2603_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2603_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2603_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2603_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2603_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2603_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2603_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2603_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2603.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2603.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2603.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2603.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2603_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2603_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2603_latest.md?ref=main

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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 單一個股分析
- score_interpretation_zh: 目前缺少完整分數資料，需以價格、TDCC 與風險條件輔助判斷。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 單一個股分析 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 單一個股分析 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 194.5
- high: 196
- low: 193
- close: 193
- volume: 16196533
- ma5: 212
- ema23_primary: 216.01
- distance_to_ema23_pct: -10.65
- ma20: 219.75
- ma60: 209.3
- ma120: 202.37
- return_5d: -14.6
- return_20d: -8.96
- volume_ratio: 0.56
- distance_to_ma20_pct_auxiliary: -12.17
- distance_to_high_60_pct: -20.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,214.5,219,214,219,30119281,207.22,5.69,207.18,205.85,2.03
20260525,220,222,214,214,31059614,207.78,2.99,207.8,206.24,1.96
20260526,215.5,218.5,211.5,211.5,27903221,208.09,1.64,208.4,206.57,1.66
20260527,213,216.5,209,211.5,33951659,208.38,1.5,208.97,206.81,1.87
20260528,212,215,211,211,27762878,208.6,1.15,209.45,206.82,1.44
20260529,212.5,216.5,211,213,30658046,208.96,1.93,210,206.77,1.5
20260601,217,225,216.5,224,38077211,210.22,6.56,210.9,207.01,1.76
20260602,225,231,220.5,231,35901526,211.95,8.99,212.05,207.39,1.57
20260603,233,242.5,228.5,237,38862223,214.04,10.73,213.3,207.83,1.61
20260604,237,240.5,231,236,27370783,215.87,9.33,214.43,208.26,1.1
20260605,239,241,232,232,23664933,217.21,6.81,215.45,208.7,0.93
20260608,222,228.5,222,224,22448385,217.78,2.86,215.95,208.93,0.86
20260609,226.5,228,221,222,22446254,218.13,1.78,216.35,209.11,0.84
20260610,223.5,225.5,221,223,21589807,218.53,2.04,217,209.37,0.79
20260611,223.5,227.5,222,226,22523796,219.16,3.12,217.72,209.49,0.8
20260612,227,232,226.5,228,18918943,219.89,3.69,219.1,209.66,0.68
20260615,230,230.5,223.5,224.5,20566934,220.28,1.92,220.45,209.77,0.74
20260616,223,223,219,220.5,32459152,220.3,0.09,221.62,209.82,1.13
20260617,198,198,192,194,60644249,218.1,-11.05,220.7,209.48,2.06
20260618,194.5,196,193,193,16196533,216.01,-10.65,219.75,209.3,0.56
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 71.16
- over_600_ratio: 69.44
- over_800_ratio: 67.95
- over_1000_ratio: 66.43
- over_400_change_1w: -1.59
- over_800_change_1w: -1.58
- over_1000_change_1w: -1.57
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.15,,64.76,,62.97,,0,False,False
20260508,69.08,0.93,65.67,0.91,64.01,1.04,1,True,True
20260515,69.37,0.29,66.08,0.41,64.41,0.4,2,True,True
20260522,69.65,0.28,66.28,0.2,64.77,0.36,3,True,True
20260529,70.63,0.98,67.41,1.13,65.92,1.15,4,True,True
20260605,72.5,1.87,69.32,1.91,67.87,1.95,5,True,True
20260612,72.75,0.25,69.53,0.21,68,0.13,6,True,True
20260618,71.16,-1.59,67.95,-1.58,66.43,-1.57,0,False,False
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| status |
| --- |
| no rows |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2603 | 長榮 | 123 | 2 | 6391300.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
