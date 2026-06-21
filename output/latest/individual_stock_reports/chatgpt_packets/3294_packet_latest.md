# INDIVIDUAL STOCK CHATGPT PACKET - 3294 英濟

## Metadata
- generated_at: 2026-06-21 22:23:23 Asia/Taipei
- stock_id: 3294
- stock_name: 英濟
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 152
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3294_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3294_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3294.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3294.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3294.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3294.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3294_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3294_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3294_latest.md?ref=main

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
- date: 20260618
- open: 41
- high: 41.5
- low: 39.4
- close: 39.7
- volume: 1577000
- ma5: 38.6
- ema23_primary: 38
- distance_to_ema23_pct: 4.47
- ma20: 39.2
- ma60: 34.94
- ma120: 36.8
- return_5d: 11.83
- return_20d: -2.34
- volume_ratio: 2
- distance_to_ma20_pct_auxiliary: 1.27
- distance_to_high_60_pct: -11.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,40.45,42.15,39.6,41.1,41000,34.86,17.89,33.37,34.41,0.02
20260525,41.2,44.95,40.45,42.3,43000,35.48,19.21,33.95,34.46,0.02
20260526,42.5,43,39.75,40.5,41000,35.9,12.81,34.44,34.49,0.02
20260527,40.9,41.15,39.5,39.8,40000,36.23,9.87,34.89,34.5,0.02
20260528,40.05,40.9,38.5,39.35,40000,36.49,7.85,35.33,34.48,0.02
20260529,40.35,40.65,39.35,40.2,40000,36.8,9.25,35.82,34.5,0.02
20260601,41,42.95,40.15,40.2,41000,37.08,8.42,36.3,34.56,0.02
20260602,40.45,42.6,40.25,41.15,42,37.42,9.97,36.81,34.62,0
20260603,41.5,41.8,40.3,40.75,41000,37.7,8.1,37.33,34.67,0.02
20260604,40.75,41.1,39.2,39.4,40000,37.84,4.13,37.73,34.74,0.02
20260605,39.4,39.4,37.7,38.3,38000,37.88,1.12,38.13,34.77,0.02
20260608,34.7,37.35,34.6,36.75,1292000,37.78,-2.73,38.44,34.74,0.55
20260609,36.65,39.35,36.35,38.75,1462000,37.86,2.34,38.82,34.77,0.61
20260610,38.4,40.25,37,37,1769000,37.79,-2.09,39.16,34.76,0.72
20260611,36.6,37.35,35.2,35.5,1007000,37.6,-5.59,39.27,34.74,0.41
20260612,36.6,36.8,35.85,35.85,646000,37.45,-4.28,39.24,34.72,0.28
20260615,37.5,39.4,37.5,39.4,2376000,37.62,4.74,39.35,34.75,1.31
20260616,41,41.1,38.15,38.15,2381000,37.66,1.3,39.28,34.78,1.58
20260617,38.15,41.05,38.15,39.9,2819000,37.85,5.42,39.25,34.85,2.54
20260618,41,41.5,39.4,39.7,1577000,38,4.47,39.2,34.94,2
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 53.21
- over_600_ratio: 50.97
- over_800_ratio: 49.9
- over_1000_ratio: 47.06
- over_400_change_1w: 0.39
- over_800_change_1w: 0
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.17,,50.62,,47.16,,0,False,False
20260508,53.34,0.17,50.74,0.12,47.91,0.75,1,True,True
20260515,53.59,0.25,50.64,-0.1,47.06,-0.85,2,False,False
20260522,52.03,-1.56,49.04,-1.6,46.21,-0.85,0,False,False
20260529,52.07,0.04,49.14,0.1,47.03,0.82,1,True,True
20260605,52.25,0.18,49.17,0.03,47.06,0.03,2,True,True
20260612,52.82,0.57,49.9,0.73,47.1,0.04,3,True,True
20260618,53.21,0.39,49.9,0,47.06,-0.04,4,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3294 | 英濟 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.發生變動日期:115/06/18 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、 自然人董事或自然人監察人）:法人董事、自然人監察人 3.舊任者職稱及姓名: 法人董事：英濟股份有限公司代表人徐文麟 法人董事：英濟股份有限公司代表人姜同會 自然人董事：增田麻言 自然人監察人：張嘉正 4.舊任者簡歷: 徐文麟：英濟股份有限公司董事長 姜同會：英濟股份有限公司總經理 增田麻言：Barintec Co., Ltd.董事長 張嘉正：英濟股份有限公司財務長 5.新任者職稱及姓名: 法人董事：英濟股份有限公司代表人徐文麟 自然人監察人：張嘉正 6.新任者簡歷: 徐文麟：英濟股份有限公司董事長 張嘉正：英濟股份有限公司財務長 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿改選 9.新任者選任時持股數: 法人董事：英濟股份有限公司代表人徐文麟-1,498,699股 自然人監察人：張嘉正-0股 10.原任期（例xx/xx/xx ~ xx/xx/xx）:112/04/25~115/04/24 11.新任生效日期:115/06/18~118/06/17 12.同任期董事變動比率:2/3 13.同任期獨立董事變動比率:不適用 14.同任期監察人變動比率:0 15.屬三分之一以上董事發生變動（請輸入是或否）:是 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第6款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3294 | 英濟 | 1 | 1 | 1 | 3 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
