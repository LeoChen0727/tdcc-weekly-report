# INDIVIDUAL STOCK CHATGPT PACKET - 4973 廣穎電通

## Metadata
- generated_at: 2026-07-01 22:28:03 Asia/Taipei
- stock_id: 4973
- stock_name: 廣穎電通
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 160
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4973_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4973_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4973_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4973_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4973_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4973_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4973_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4973_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4973_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4973_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4973_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4973_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4973.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4973.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4973.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4973.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4973_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4973_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4973_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260701
- open: 176
- high: 176.5
- low: 160
- close: 160
- volume: 4396000
- ma5: 172.8
- ema23_primary: 170.28
- distance_to_ema23_pct: -6.04
- ma20: 181.95
- ma60: 128.48
- ma120: 91.16
- return_5d: -13.51
- return_20d: 2.24
- volume_ratio: 1.47
- distance_to_ma20_pct_auxiliary: -12.06
- distance_to_high_60_pct: -26.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,172,172,166,172,171000,126.13,36.37,126,92.76,0.04
20260604,171,178.5,171,176,175000,130.28,35.09,130.03,94.93,0.04
20260605,173.5,173.5,160,171.5,168000,133.72,28.25,133.62,96.94,0.05
20260608,154.5,162,154.5,160,2032000,135.91,17.73,136.15,98.68,0.65
20260609,166.5,176,166,176,2057000,139.25,26.39,138.95,100.6,0.79
20260610,186.5,193.5,186.5,193,4668000,143.73,34.28,142.68,102.69,1.97
20260611,191.5,194,175,191.5,3581000,147.71,29.65,146.43,104.65,1.8
20260612,198.5,199,191,191,2169000,151.32,26.22,150.12,106.48,1.26
20260615,195.5,210,192.5,210,3089000,156.21,34.44,154.6,108.5,1.88
20260616,210,219,189,189.5,9494000,158.98,19.2,158.57,110.02,5.22
20260617,185,191.5,180.5,191.5,4196000,161.69,18.43,162.7,111.73,2.29
20260618,192.5,197.5,188,193.5,3896000,164.34,17.74,166.97,113.63,2.13
20260622,195.5,197,190,191.5,3803000,166.61,14.94,170.8,115.63,1.88
20260623,192,192,180.5,183,3696000,167.97,8.95,174.05,117.5,1.68
20260624,180.5,187,180.5,185,2211000,169.39,9.21,176.97,119.51,0.96
20260625,189.5,191,181,182,2219000,170.44,6.78,179.12,121.53,0.92
20260626,184,189,178,180,2899000,171.24,5.12,180.5,123.41,1.14
20260629,180.5,181,168.5,168.5,3188000,171.01,-1.47,180.93,125.18,1.18
20260630,172,174,168.5,173.5,1697000,171.22,1.33,181.78,126.94,0.61
20260701,176,176.5,160,160,4396000,170.28,-6.04,181.95,128.48,1.47
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 25.01
- over_600_ratio: 21.97
- over_800_ratio: 17.71
- over_1000_ratio: 16.25
- over_400_change_1w: -1.53
- over_800_change_1w: -1.45
- over_1000_change_1w: -0.16
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,30.65,,23.5,,19.27,,0,False,False
20260508,33.54,2.89,22.2,-1.3,19.27,0,1,False,False
20260515,32.09,-1.45,24.89,2.69,19.27,0,2,False,True
20260522,33.51,1.42,24.11,-0.78,21.34,2.07,3,False,True
20260529,36.19,2.68,23.42,-0.69,21.96,0.62,4,False,True
20260605,31.22,-4.97,22.95,-0.47,18.56,-3.4,0,False,False
20260612,31.49,0.27,23.01,0.06,20.26,1.7,1,True,True
20260618,26.54,-4.95,19.16,-3.85,16.41,-3.85,0,False,False
20260626,25.01,-1.53,17.71,-1.45,16.25,-0.16,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 4973 | 廣穎電通 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  |  | repeated_but_no_breakout | 1.發生變動日期:115/06/18 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名: (1)黃清茂 (2)洪敬恒 (3)劉復華 (4)鄭翠玉 4.舊任者簡歷: (1)黃清茂：泰博科技股份有限公司特別助理 (2)洪敬恒：太曼妮企業有限公司代表人 (3)劉復華：頂典有限公司代表人 (4)鄭翠玉：廣展會計師事務所所長 5.新任者姓名: (1)黃清茂 (2)洪敬恒 (3)鄭翠玉 (4)許源卿 6.新任者簡歷: (1)黃清茂：泰博科技股份有限公司特別助理 (2)洪敬恒：太曼妮企業有限公司代表人 (3)鄭翠玉：廣展會計師事務所所長 (4)許源卿：昇佳電子股份有限公司營運長 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿，全面改選。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/18~115/06/17 10.新任生效日期:115/06/18 11.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 4973 | 廣穎電通 | 8 | 7 | 5 | 8 | 9 | repeated_but_no_breakout | 近 10 日上榜 8 次、近 20 日上榜 9 次，但尚未有效突破，需等待攻擊確認。 |

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
