# INDIVIDUAL STOCK CHATGPT PACKET - 2527 宏璟

## Metadata
- generated_at: 2026-06-30 22:26:46 Asia/Taipei
- stock_id: 2527
- stock_name: 宏璟
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 294
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2527_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2527_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2527_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2527_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2527_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2527_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2527_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2527_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2527_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2527_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2527_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2527_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2527.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2527.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2527.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2527.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2527_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2527_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2527_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- none

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260630
- open: 39.3
- high: 40.85
- low: 39.3
- close: 40.7
- volume: 1294000
- ma5: 40.07
- ema23_primary: 38.07
- distance_to_ema23_pct: 6.9
- ma20: 37.98
- ma60: 35.69
- ma120: 32.71
- return_5d: 2.52
- return_20d: 10.75
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: 7.16
- distance_to_high_60_pct: -1.93

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,37,37,36.05,36.6,395300,34.89,4.89,34.6,33.02,0.8
20260603,37.2,37.4,36.85,37.25,621953,35.09,6.16,34.77,33.13,1.23
20260604,37.5,37.5,36.65,37,328350,35.25,4.97,34.88,33.26,0.66
20260605,36.6,36.65,36,36.35,358492,35.34,2.86,34.97,33.37,0.72
20260608,34.4,34.8,33.9,34.55,364033,35.27,-2.05,34.98,33.45,0.79
20260609,34.6,35.25,34.6,35.05,336973,35.26,-0.58,35.05,33.55,0.77
20260610,34.45,35.95,34.2,34.6,697747,35.2,-1.71,35.07,33.64,1.54
20260611,34.8,35.35,34.15,34.6,322398,35.15,-1.57,35.13,33.72,0.72
20260612,35,37,35,36.5,701326,35.26,3.51,35.3,33.83,1.52
20260615,36.55,39.85,36,39.15,2294490,35.59,10.01,35.57,33.97,4.1
20260616,40.3,40.75,39.5,39.95,5496568,35.95,11.12,35.91,34.14,6.63
20260617,39.35,39.35,38.25,38.9,1569832,36.2,7.47,36.2,34.29,1.75
20260618,39,40.45,39,39.8,2006523,36.5,9.05,36.52,34.47,2.04
20260622,40,40,38.85,39.25,1189522,36.73,6.87,36.81,34.64,1.16
20260623,39.85,41.05,39.45,39.7,1951844,36.97,7.37,37.05,34.81,1.79
20260624,39.25,39.95,39.1,39.7,952209,37.2,6.72,37.27,34.98,0.85
20260625,40.1,41,39.75,40.15,1110462,37.45,7.22,37.47,35.16,0.98
20260626,39.8,41.5,39.55,40.35,2370977,37.69,7.06,37.65,35.34,1.96
20260629,40.35,40.75,39.15,39.45,1052677,37.84,4.27,37.78,35.52,0.86
20260630,39.3,40.85,39.3,40.7,1294000,38.07,6.9,37.98,35.69,1.02
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 79.82
- over_600_ratio: 77.6
- over_800_ratio: 75.85
- over_1000_ratio: 74.89
- over_400_change_1w: 0.39
- over_800_change_1w: 0.13
- over_1000_change_1w: 0.44
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.96,,75.73,,74,,0,False,False
20260508,79.76,-0.2,75.68,-0.05,74.01,0.01,1,False,True
20260515,79.52,-0.24,75.11,-0.57,74.44,0.43,2,False,True
20260522,79.69,0.17,75.12,0.01,74.45,0.01,3,True,True
20260529,80.09,0.4,75.78,0.66,74.46,0.01,4,True,True
20260605,80.04,-0.05,76.15,0.37,74.49,0.03,5,False,True
20260612,79.82,-0.22,75.83,-0.32,74.49,0,0,False,False
20260618,79.43,-0.39,75.72,-0.11,74.45,-0.04,0,False,False
20260626,79.82,0.39,75.85,0.13,74.89,0.44,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 2527 | 宏璟 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_2_3d | 1.發生變動日期:115/06/26 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:法人董事、自然人董事、自然人監察人 3.舊任者職稱及姓名: (1)董事    A.宏璟建設(股)公司代表人：周家佩    B.宏璟建設(股)公司代表人：陳芳瑩    C.宏璟建設(股)公司代表人：蘇經洲    D.雷淑燕    E.龔?蓮 (2)監察人    A.姚筱薇    B.黃朝樑 4.舊任者簡歷: (1)董事    A.宏璟建設(股)公司代表人：周家佩-宏璟建設(股)公司總經理    B.宏璟建設(股)公司代表人：陳芳瑩-宏璟建設(股)公司財務處副總經理    C.宏璟建設(股)公司代表人：蘇經洲-宏璟建設(股)公司中壢工區副總經理    D.雷淑燕-宏璟建設(股)公司業務處經理    E.龔?蓮-宏璟建設(股)公司財務處經理 (2)監察人    A.姚筱薇-宏璟建設(股)公司業務處副總經理    B.黃朝樑-宏璟建設(股)公司竹北工區協理 5.新任者職稱及姓名: (1)董事    A.宏璟建設(股)公司代表人：周家佩    B.宏璟建設(股)公司代表人：陳芳瑩    C.宏璟建設(股)公司代表人：潘順完    D.雷淑燕    E.龔?蓮 (2)監察人    A.姚筱薇    B.黃朝樑 6.新任者簡歷: (1)董事    A.宏璟建設(股)公司代表人：周家佩-宏璟建設(股)公司總經理    B.宏璟建設(股)公司代表人：陳芳瑩-宏璟建設(股)公司財務處副總經理    C.宏璟建設(股)公司代表人：潘順完-宏璟建設(股)公司開發處副總經理    D.雷淑燕-宏璟建設(股)公司業務處經理    E.龔?蓮-宏璟建設(股)公司財務處經理 (2)監察人    A.姚筱薇-宏璟建設(股)公司業務處副總經理    B.黃朝樑-宏璟建設(股)公司竹北工區協理 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:配合股東會召開時間，提前全面改選 9.新任者選任時持股數: (1)董事   A.宏璟建設(股)公司-208,853,490股     代表人：周家佩-0股   B.宏璟建設(股)公司-208,853,490股     代表人：陳芳瑩-0股   C.宏璟建設(股)公司-208,853,490股     代表人：潘順完-0股   D.雷淑燕-0股   E.龔?蓮-0股 (2)監察人   A.姚筱薇-0股   B.黃朝樑-0股 10.原任期（例xx/xx/xx ~ xx/xx/xx）:112/12/22-115/12/21 11.新任生效日期:115/06/26 12.同任期董事變動比率:不適用 13.同任期獨立董事變動比率:不適用 14.同任期監察人變動比率:不適用 15.屬三分之一以上董事發生變動（請輸入是或否）:否 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 2527 | 宏璟 | 3 | 1 | 4 | 8 | 8 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
