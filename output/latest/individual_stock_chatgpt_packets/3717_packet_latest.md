# INDIVIDUAL STOCK CHATGPT PACKET - 3717 聯嘉投控

## Metadata
- generated_at: 2026-06-17 22:23:53 Asia/Taipei
- stock_id: 3717
- stock_name: 聯嘉投控
- packet_status: standard_180d_window_packet
- latest_price_date: 20260617
- price_rows: 193
- latest_tdcc_date: 20260612
- tdcc_rows: 7
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3717_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3717_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3717_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3717_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3717_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3717_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3717_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3717_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3717_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3717_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3717_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3717_tdcc_window_latest.txt?ref=main
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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 歷史不足、TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足、TDCC 轉弱警訊

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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260617
- open: 21.7
- high: 23.8
- low: 21.7
- close: 22.45
- volume: 19629286
- ma5: 21.38
- ema23_primary: 22.1
- distance_to_ema23_pct: 1.57
- ma20: 22.39
- ma60: 21.94
- ma120: 19.8
- return_5d: 0.9
- return_20d: 1.35
- volume_ratio: 5.56
- distance_to_ma20_pct_auxiliary: 0.29
- distance_to_high_60_pct: -10.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260518,22.1,23.15,21.7,22.45,2708300,21.96,2.22,21.8,20.5,1.25
20260519,22.55,23.55,22.4,22.5,1979909,22.01,2.24,21.8,20.58,0.9
20260520,22.8,23.25,22.7,23.05,1638222,22.09,4.33,21.84,20.67,0.73
20260521,23.55,24.3,23.1,23.75,4854715,22.23,6.83,21.92,20.78,2
20260522,24.1,25,24.05,24.65,4702922,22.43,9.88,22.1,20.9,1.82
20260525,25,25,22.95,22.95,4285479,22.48,2.11,22.21,20.99,1.55
20260526,23.5,23.5,22,22.45,2580227,22.47,-0.11,22.34,21.07,0.91
20260527,22.5,22.65,21.95,22,1744096,22.44,-1.94,22.45,21.14,0.6
20260528,22,22.4,21.4,21.6,3779536,22.37,-3.42,22.54,21.21,1.24
20260529,21.8,22.6,21.5,22.6,1489537,22.39,0.96,22.7,21.3,0.48
20260601,22.85,23.15,22.05,22.4,2246659,22.39,0.06,22.82,21.41,0.71
20260602,22.45,22.65,21.9,22.4,1655102,22.39,0.06,22.84,21.48,0.52
20260603,22.45,23.6,22.45,23.35,3678953,22.47,3.93,22.86,21.57,1.24
20260604,22.45,22.65,21.9,22.4,1655102,22.46,-0.28,22.77,21.65,0.6
20260605,22.85,22.85,22.2,22.25,1306331,22.44,-0.87,22.68,21.73,0.52
20260611,20.2,20.9,20.1,20.3,1765550,22.27,-8.83,22.53,21.76,0.73
20260612,20.6,20.65,20.25,20.25,1077483,22.1,-8.36,22.4,21.79,0.46
20260615,22,22.25,21.4,22.25,3470740,22.11,0.63,22.4,21.84,1.41
20260616,22,23.35,21.65,21.65,4310614,22.07,-1.91,22.37,21.88,1.66
20260617,21.7,23.8,21.7,22.45,19629286,22.1,1.57,22.39,21.94,5.56
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 45.27
- over_600_ratio: 40.56
- over_800_ratio: 36.88
- over_1000_ratio: 35.18
- over_400_change_1w: -0.72
- over_800_change_1w: -1.79
- over_1000_change_1w: -1.42
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
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3717 | 聯嘉投控 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:現金股利，每股配發新台幣0.197058元， 共計新台幣41,569,089元。 4.除權（息）交易日:115/07/14 5.最後過戶日:115/07/15 6.停止過戶起始日期:115/07/16 7.停止過戶截止日期:115/07/20 8.除權（息）基準日:115/07/20 9.債券最後申請轉換日期:115/06/23 10.債券停止轉換起始日期:115/06/25 11.債券停止轉換截止日期:115/07/20 12.普通股現金股利發放日期:115/08/07 13.其他應敘明事項:本公司轉換公司債停止轉換期間為115/06/25~115/07/20 ，債券持有人如擬申請轉換，最遲應於115/06/23向往來證券商辦理轉換手續。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3717 | 聯嘉投控 | 1 | 1 | 2 | 6 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
