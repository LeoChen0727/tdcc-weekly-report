# INDIVIDUAL STOCK CHATGPT PACKET - 2317 鴻海

## Metadata
- generated_at: 2026-07-12 22:26:35 Asia/Taipei
- stock_id: 2317
- stock_name: 鴻海
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 300
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2317_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2317_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2317_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2317_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2317_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2317_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2317_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2317_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2317_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2317_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2317_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2317_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2317.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2317.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2317.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2317.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2317_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2317_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2317_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: high
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
- decision_score_high
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
- date: 20260709
- open: 238
- high: 240
- low: 234.5
- close: 237.5
- volume: 40528079
- ma5: 238.9
- ema23_primary: 251.26
- distance_to_ema23_pct: -5.48
- ma20: 253.25
- ma60: 249.94
- ma120: 233.3
- return_5d: -0.63
- return_20d: -9.7
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: -6.22
- distance_to_high_60_pct: -24.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,260,262.5,251.5,258.5,97550509,265.66,-2.7,268.27,233.07,0.92
20260612,266.5,269,260,260.5,60260948,265.23,-1.78,268.88,233.88,0.59
20260615,271,272.5,265,267.5,54689024,265.42,0.78,269.82,234.83,0.54
20260616,270,271,265.5,269,56878574,265.72,1.24,271.02,235.9,0.56
20260617,266,272,264,272,42755242,266.24,2.16,272.62,237.05,0.43
20260618,270.5,271.5,268.5,268.5,68996866,266.43,0.78,273.68,238.26,0.68
20260622,270,275.5,268.5,268.5,67145972,266.6,0.71,274.6,239.48,0.66
20260623,270,270.5,259,259.5,92063800,266.01,-2.45,274.52,240.47,0.92
20260624,255,261,255,256,63690545,265.18,-3.46,274.38,241.4,0.64
20260625,260.5,262.5,257.5,257.5,43578494,264.54,-2.66,274.05,242.37,0.44
20260626,255.5,255.5,248,248.5,80450955,263.2,-5.58,273.32,243.28,0.81
20260629,250,252,246,246.5,49210311,261.81,-5.85,271.2,244.26,0.57
20260630,251.5,255.5,249,251,51113000,260.91,-3.8,269.07,245.16,0.65
20260701,255,255.5,248,248,63410000,259.83,-4.55,266.4,246.07,0.83
20260702,239,243,238,239,64466000,258.1,-7.4,262.9,246.86,0.89
20260703,237,241,236,240.5,51008242,256.63,-6.29,260.27,247.51,0.74
20260706,243.5,247.5,240.5,242,42156000,255.41,-5.25,258.15,248.21,0.63
20260707,243,243,236,237,51778760,253.88,-6.65,256.52,248.82,0.82
20260708,240,240.5,234,237.5,37939126,252.51,-5.94,254.53,249.44,0.62
20260709,238,240,234.5,237.5,40528079,251.26,-5.48,253.25,249.94,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 69.05
- over_600_ratio: 67.92
- over_800_ratio: 67.11
- over_1000_ratio: 66.38
- over_400_change_1w: -0.88
- over_800_change_1w: -0.85
- over_1000_change_1w: -0.84
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.6,,65.63,,64.91,,0,False,False
20260508,69.22,1.62,67.22,1.59,66.52,1.61,1,True,True
20260515,69.39,0.17,67.41,0.19,66.71,0.19,2,True,True
20260522,69.76,0.37,67.81,0.4,67.07,0.36,3,True,True
20260529,70.43,0.67,68.48,0.67,67.79,0.72,4,True,True
20260605,70.96,0.53,69.05,0.57,68.31,0.52,5,True,True
20260612,70.52,-0.44,68.59,-0.46,67.84,-0.47,0,False,False
20260618,70.47,-0.05,68.56,-0.03,67.82,-0.02,0,False,False
20260626,69.93,-0.54,67.96,-0.6,67.22,-0.6,0,False,False
20260703,69.05,-0.88,67.11,-0.85,66.38,-0.84,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2317 | 鴻海 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  | no_signal | stale_signal | 1.發生變動日期:115/07/10 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:法人董事 3.舊任者職稱及姓名:鴻景國際投資股份有限公司(代表人：劉憶如) 4.舊任者簡歷:本公司法人董事 5.新任者職稱及姓名:不適用 6.新任者簡歷:不適用 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 辭職 8.異動原因:因整體規劃考量，鴻景國際投資股份有限公司辭任由劉憶如女士擔任 法人代表人之董事職務。 9.新任者選任時持股數:不適用 10.原任期（例xx/xx/xx ~ xx/xx/xx）:114/05/29~117/05/28 11.新任生效日期:不適用 12.同任期董事變動比率:2/9 13.同任期獨立董事變動比率:1/5 14.同任期監察人變動比率:不適用 15.屬三分之一以上董事發生變動（請輸入是或否）:否 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項): 鴻景國際投資股份有限公司現擔任本公司董事二席，本次僅辭任前述一席董事 職務，保留其餘一席董事職務，並由原法人代表人繼續擔任。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260709 | 2317 | 鴻海 | revenue_breakout_low_response | 營收爆發低反應股 | 10.0 | 36.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.發生變動日期:115/07/10 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:法人董事 3.舊任者職稱及姓名:鴻景國際投資股份有限公司(代表人：劉憶如) 4.舊任者簡歷:本公司法人董事 5.新任者職稱及姓名:不適用 6.新任者簡歷:不適用 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 辭職 8.異動原因:因整體規劃考量，鴻景國際投資股份有限公司辭任由劉憶如女士擔任 法人代表人之董事職務。 9.新任者選任時持股數:不適用 10.原任期（例xx/xx/xx ~ xx/xx/xx）:114/05/29~117/05/28 11.新任生效日期:不適用 12.同任期董事變動比率:2/9 13.同任期獨立董事變動比率:1/5 14.同任期監察人變動比率:不適用 15.屬三分之一以上董事發生變動（請輸入是或否）:否 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項): 鴻景國際投資股份有限公司現擔任本公司董事二席，本次僅辭任前述一席董事 職務，保留其餘一席董事職務，並由原法人代表人繼續擔任。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2317 | 鴻海 | 6 | 6 | 5 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2317 | 鴻海 | 516 | 40 | 24833470.0 | 236250.0 | 105.12 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
