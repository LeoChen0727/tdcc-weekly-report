# INDIVIDUAL STOCK CHATGPT PACKET - 2889 國票金

## Metadata
- generated_at: 2026-06-21 22:23:11 Asia/Taipei
- stock_id: 2889
- stock_name: 國票金
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2889_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2889_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2889.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2889.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2889.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2889.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2889_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2889_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2889_latest.md?ref=main

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
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260618
- open: 15.2
- high: 15.35
- low: 15.15
- close: 15.25
- volume: 7205938
- ma5: 15.12
- ema23_primary: 14.95
- distance_to_ema23_pct: 2.02
- ma20: 14.89
- ma60: 14.99
- ma120: 15.76
- return_5d: 2.01
- return_20d: 3.39
- volume_ratio: 1.17
- distance_to_ma20_pct_auxiliary: 2.42
- distance_to_high_60_pct: -12.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,14.65,14.85,14.6,14.65,1892071,14.78,-0.88,14.62,15.46,0.61
20260525,14.7,14.7,14.5,14.55,2373133,14.76,-1.43,14.62,15.42,0.78
20260526,14.55,14.7,14.5,14.6,2233519,14.75,-1,14.63,15.38,0.82
20260527,14.6,14.7,14.5,14.55,3074575,14.73,-1.23,14.62,15.34,1.12
20260528,14.6,14.7,14.5,14.6,3705911,14.72,-0.82,14.62,15.31,1.31
20260529,14.6,14.7,14.55,14.7,2933836,14.72,-0.13,14.62,15.28,1.07
20260601,14.7,14.75,14.55,14.75,4540964,14.72,0.2,14.63,15.25,1.61
20260602,14.65,14.8,14.5,14.75,5203169,14.72,0.18,14.64,15.23,1.76
20260603,14.75,15.2,14.65,15.15,9916351,14.76,2.65,14.68,15.21,2.98
20260604,15.15,15.2,14.95,15.15,5669719,14.79,2.42,14.71,15.21,1.63
20260605,15.15,15.2,14.9,15.05,5975487,14.81,1.6,14.72,15.19,1.63
20260608,14.6,14.9,14.55,14.7,8269955,14.8,-0.7,14.72,15.16,2.15
20260609,14.65,15.1,14.65,15,7546510,14.82,1.21,14.73,15.14,1.87
20260610,15,15.2,14.95,15.05,9037478,14.84,1.42,14.75,15.12,2.06
20260611,15.1,15.1,14.85,14.95,5710056,14.85,0.68,14.77,15.09,1.27
20260612,15,15.15,14.9,15,8138925,14.86,0.93,14.79,15.07,1.72
20260615,15.1,15.2,14.95,15.05,8033924,14.88,1.16,14.82,15.05,1.59
20260616,15.05,15.2,15,15.1,9157478,14.9,1.37,14.84,15.04,1.7
20260617,15.1,15.4,15.05,15.2,12557868,14.92,1.87,14.87,15.01,2.13
20260618,15.2,15.35,15.15,15.25,7205938,14.95,2.02,14.89,14.99,1.17
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 74.13
- over_600_ratio: 73.12
- over_800_ratio: 72.26
- over_1000_ratio: 71.62
- over_400_change_1w: -0.15
- over_800_change_1w: -0.17
- over_1000_change_1w: -0.17
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,74.57,,72.64,,72.03,,0,False,False
20260508,74.45,-0.12,72.59,-0.05,71.98,-0.05,0,False,False
20260515,74.36,-0.09,72.51,-0.08,71.87,-0.11,0,False,False
20260522,74.4,0.04,72.58,0.07,71.94,0.07,1,True,True
20260529,74.39,-0.01,72.52,-0.06,71.9,-0.04,0,False,False
20260605,74.39,0,72.51,-0.01,71.87,-0.03,0,False,False
20260612,74.28,-0.11,72.43,-0.08,71.79,-0.08,0,False,False
20260618,74.13,-0.15,72.26,-0.17,71.62,-0.17,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2889 | 國票金 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.董事會決議日期或發生變動日期:115/06/15 2.人員別（請輸入董事長或總經理）:董事長 3.舊任者姓名:董事長 魏啟林 4.舊任者簡歷:國票金融控股股份有限公司 董事長 5.新任者姓名:NA 6.新任者簡歷:NA 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「職務調整」、「資遣」、 「退休」、「逝世」或「新任」）:退休 8.異動原因:申請退休 9.新任生效日期:NA 10.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項): 預定第17屆董事會第37次會議改選董事長；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2889 | 國票金 | 17 | 3 | 5 | 10 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
