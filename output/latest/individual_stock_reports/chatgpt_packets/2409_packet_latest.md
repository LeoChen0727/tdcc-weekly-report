# INDIVIDUAL STOCK CHATGPT PACKET - 2409 友達

## Metadata
- generated_at: 2026-06-21 22:22:57 Asia/Taipei
- stock_id: 2409
- stock_name: 友達
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2409_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2409_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2409_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2409_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2409_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2409_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2409_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2409_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2409_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2409_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2409_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2409_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2409.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2409.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2409.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2409.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2409_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2409_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2409_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260618
- open: 27.45
- high: 28.6
- low: 26.05
- close: 28.15
- volume: 828311957
- ma5: 25.18
- ema23_primary: 23.79
- distance_to_ema23_pct: 18.34
- ma20: 24.5
- ma60: 20.08
- ma120: 17.38
- return_5d: 21.6
- return_20d: 39.36
- volume_ratio: 1.7
- distance_to_ma20_pct_auxiliary: 14.89
- distance_to_high_60_pct: -4.9

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,20.85,22.2,20.55,22.2,394425774,18.95,17.14,18.66,17.34,1.46
20260525,24.35,24.4,24.15,24.4,82302936,19.41,25.73,19.02,17.47,0.31
20260526,25.5,25.8,22,22,818361725,19.62,12.12,19.25,17.57,2.77
20260527,22.15,22.2,20.5,21.8,566175271,19.8,10.08,19.48,17.66,1.78
20260528,21.9,23.4,21.2,21.2,538705306,19.92,6.42,19.68,17.73,1.59
20260529,22.35,23.2,21.9,23,481574851,20.18,13.99,19.97,17.85,1.35
20260601,23.8,24.8,23.1,23.8,564845158,20.48,16.22,20.31,18,1.5
20260602,24.05,26.15,23.3,26.15,720567401,20.95,24.81,20.73,18.18,1.81
20260603,27.5,28.75,26.7,28.75,706729442,21.6,33.09,21.26,18.39,1.68
20260604,28.4,29.6,27.5,29.25,878685417,22.24,31.53,21.8,18.62,1.94
20260605,28,28.4,26.35,27.1,607774938,22.64,19.68,22.27,18.81,1.29
20260608,24.4,24.4,24.4,24.4,69133057,22.79,7.06,22.55,18.94,0.15
20260609,25,25.2,24,24,505972455,22.89,4.84,22.71,19.05,1.13
20260610,23.4,24.7,22.85,22.95,368098295,22.9,0.24,22.85,19.16,0.83
20260611,22.75,23.75,22.2,23.15,320575053,22.92,1.02,23.03,19.28,0.73
20260612,24.6,25,23.45,23.5,300437623,22.97,2.33,23.25,19.41,0.68
20260615,24.45,25,24.1,24.1,234168728,23.06,4.51,23.49,19.54,0.53
20260616,24.5,24.75,23.9,23.9,203629435,23.13,3.33,23.73,19.68,0.46
20260617,23.6,26.25,23.35,26.25,559042864,23.39,12.23,24.11,19.85,1.2
20260618,27.45,28.6,26.05,28.15,828311957,23.79,18.34,24.5,20.08,1.7
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 50.13
- over_600_ratio: 47.89
- over_800_ratio: 46.58
- over_1000_ratio: 45.37
- over_400_change_1w: 1.83
- over_800_change_1w: 1.82
- over_1000_change_1w: 1.87
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.96,,46.02,,44.82,,0,False,False
20260508,49.63,-0.33,45.72,-0.3,44.54,-0.28,0,False,False
20260515,51.44,1.81,47.61,1.89,46.47,1.93,1,True,True
20260522,53.08,1.64,49.43,1.82,48.24,1.77,2,True,True
20260529,50.39,-2.69,46.86,-2.57,45.59,-2.65,0,False,False
20260605,51.58,1.19,48,1.14,46.56,0.97,1,True,True
20260612,48.3,-3.28,44.76,-3.24,43.5,-3.06,0,False,False
20260618,50.13,1.83,46.58,1.82,45.37,1.87,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2409 | 友達 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_put_bullish | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/06/22 1.召開法人說明會之日期：115/06/22 ~ 115/06/26 2.召開法人說明會之時間：16 時 00 分  3.召開法人說明會之地點：倫敦、蘇黎士、巴黎 4.法人說明會擇要訊息：本公司將參加J.P Morgan舉辦之「Asia Pacific All Star Forum – London」以及 「Non-Deal Roadshow」，就115年第一季法說會之內容說明公司營運與財務概況。 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2409 | 友達 | 1 | 1 | 4 | 6 | 10 | repeated_but_no_breakout | 近 10 日上榜 6 次、近 20 日上榜 10 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2409 | 友達 | 231 | 12 | 80527190.0 | 433340.0 | 185.83 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
