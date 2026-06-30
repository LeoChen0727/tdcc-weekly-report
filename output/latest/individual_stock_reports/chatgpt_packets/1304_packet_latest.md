# INDIVIDUAL STOCK CHATGPT PACKET - 1304 台聚

## Metadata
- generated_at: 2026-06-30 22:26:13 Asia/Taipei
- stock_id: 1304
- stock_name: 台聚
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 294
- latest_tdcc_date: 20260626
- tdcc_rows: 31
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1304_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1304_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1304_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1304_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1304_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1304_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1304_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1304_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1304_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1304_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1304_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1304_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1304.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1304.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1304.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1304.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1304_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1304_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1304_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260630
- open: 13.4
- high: 13.6
- low: 13.2
- close: 13.55
- volume: 4535000
- ma5: 13.39
- ema23_primary: 13.14
- distance_to_ema23_pct: 3.11
- ma20: 13.18
- ma60: 13.65
- ma120: 13.11
- return_5d: 5.86
- return_20d: 4.23
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 2.81
- distance_to_high_60_pct: -27.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,13.4,13.4,12.95,13.3,10417981,12.88,3.29,12.55,14.11,1.61
20260603,13.45,14.35,13.25,14.3,18581384,13,10.04,12.61,14.12,2.65
20260604,14.15,14.45,13.65,13.7,9986479,13.05,4.95,12.64,14.12,1.43
20260605,13.55,13.75,13.1,13.4,5829064,13.08,2.43,12.68,14.13,0.83
20260608,12.65,12.85,12.5,12.8,5356061,13.06,-1.98,12.66,14.14,0.76
20260609,12.8,12.85,12.55,12.75,4478971,13.03,-2.17,12.66,14.13,0.63
20260610,12.65,12.85,12.55,12.75,3271955,13.01,-2,12.65,14.13,0.47
20260611,12.95,13,12.4,12.5,3508736,12.97,-3.6,12.64,14.12,0.51
20260612,12.6,12.9,12.5,12.7,3633161,12.95,-1.89,12.66,14.12,0.53
20260615,12.8,12.85,12.55,12.7,4593878,12.92,-1.74,12.67,14.12,0.69
20260616,12.7,12.95,12.6,12.75,3968461,12.91,-1.24,12.7,14.09,0.6
20260617,12.8,13.1,12.65,12.95,4724951,12.91,0.28,12.74,14.06,0.71
20260618,13.15,13.95,13.05,13.55,9380424,12.97,4.5,12.81,14.01,1.36
20260622,13.8,14.05,13.6,13.7,8383029,13.03,5.16,12.88,13.98,1.19
20260623,13.6,13.6,12.8,12.8,7367480,13.01,-1.6,12.91,13.95,1.03
20260624,12.7,13.65,12.6,13.6,7614634,13.06,4.15,12.98,13.92,1.05
20260625,13.6,14,13.4,13.4,6613630,13.09,2.4,13.06,13.87,0.89
20260626,13.45,13.6,13,13.2,5259253,13.1,0.8,13.1,13.79,0.74
20260629,13.25,13.4,13.05,13.2,3093252,13.1,0.73,13.15,13.71,0.45
20260630,13.4,13.6,13.2,13.55,4535000,13.14,3.11,13.18,13.65,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 61.29
- over_600_ratio: 59.8
- over_800_ratio: 58.78
- over_1000_ratio: 58.18
- over_400_change_1w: 0.43
- over_800_change_1w: 0.27
- over_1000_change_1w: 0.26
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260410,59.18,-0.4,56.77,-0.56,56.03,-0.68,0,False,False
20260417,59.48,0.3,57.03,0.26,56.34,0.31,1,True,True
20260424,59.18,-0.3,56.86,-0.17,56.16,-0.18,0,False,False
20260430,59.36,0.18,57.08,0.22,56.56,0.4,1,True,True
20260508,59.82,0.46,57.43,0.35,56.82,0.26,2,True,True
20260515,59.99,0.17,57.73,0.3,57.05,0.23,3,True,True
20260522,60.1,0.11,57.82,0.09,57.23,0.18,4,True,True
20260529,60.12,0.02,57.62,-0.2,57.02,-0.21,5,False,False
20260605,60.62,0.5,58.25,0.63,57.65,0.63,6,True,True
20260612,60.74,0.12,58.45,0.2,57.86,0.21,7,True,True
20260618,60.86,0.12,58.51,0.06,57.92,0.06,8,True,True
20260626,61.29,0.43,58.78,0.27,58.18,0.26,9,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1304 | 台聚 | pattern | 型態觀察 | 54.0 |  |  | base_building |  | no_signal | stale_signal | 1.發生變動日期:115/06/19 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:自然人董事 3.舊任者職稱及姓名:余經壽董事 4.舊任者簡歷:恆凱環球有限公司董事 5.新任者職稱及姓名:不適用 6.新任者簡歷:不適用 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）:逝世 8.異動原因:逝世 9.新任者選任時持股數:不適用 10.原任期（例xx/xx/xx ~ xx/xx/xx）:不適用 11.新任生效日期:不適用 12.同任期董事變動比率:不適用 13.同任期獨立董事變動比率:不適用 14.同任期監察人變動比率:不適用 15.屬三分之一以上董事發生變動（請輸入是或否）:否 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項):  本公司於115/06/19接獲此訊。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1304 | 台聚 | 1 | 1 | 2 | 3 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1304 | 台聚 | 46 | 0 | 822870.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
