# INDIVIDUAL STOCK CHATGPT PACKET - 4977 眾達-KY

## Metadata
- generated_at: 2026-08-22 16:00:33 Asia/Taipei
- stock_id: 4977
- stock_name: 眾達-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 337
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4977_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4977_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4977_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4977_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4977_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4977_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4977_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4977_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4977_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4977_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4977_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4977_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4977.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4977.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4977.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4977.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4977_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4977_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4977_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20260821
- open: 159
- high: 160
- low: 150
- close: 150.5
- volume: 6080444
- ma5: 152.2
- ema23_primary: 145.28
- distance_to_ema23_pct: 3.59
- ma20: 138.07
- ma60: 159.83
- ma120: 181
- return_5d: 4.51
- return_20d: 8.27
- volume_ratio: 1.73
- distance_to_ma20_pct_auxiliary: 9
- distance_to_high_60_pct: -35.27

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,135,138.5,130,133.5,4368038,150.92,-11.54,147.75,187.31,2.05
20260728,126,132,123.5,124,3177754,148.67,-16.59,145.6,185.87,1.44
20260729,123,125,112,112,2229870,145.62,-23.09,142.72,184.11,0.98
20260730,111,114,105,106.5,2353986,142.36,-25.19,140.2,182.22,1.04
20260731,116,117,112,117,1403294,140.24,-16.57,138.03,180.31,0.62
20260803,117,125.5,116,121.5,2458277,138.68,-12.39,136,178.62,1.07
20260804,125.5,132.5,125,131,3228959,138.04,-5.1,134.6,177,1.35
20260805,140,144,138.5,142.5,5144394,138.41,2.95,134.22,175.28,2.07
20260806,139.5,141.5,134,138.5,3430888,138.42,0.06,133.47,173.07,1.33
20260807,136,141.5,131.5,133.5,2134747,138.01,-3.27,132.53,171.24,0.81
20260810,134.5,145,134.5,144.5,3104053,138.55,4.29,132.18,169.72,1.14
20260811,147,153,143,146.5,5239211,139.21,5.23,132.15,168.39,1.83
20260812,147,158,147,154,5316331,140.45,9.65,132.4,167.47,1.72
20260813,158,161,150,151.5,4313153,141.37,7.17,132.78,166.62,1.32
20260814,150,150,143.5,144,1886956,141.59,1.7,133.47,165.67,0.58
20260817,147,158,143.5,158,3202647,142.95,10.53,135,164.89,0.96
20260818,157,160,149,151,4511096,143.62,5.14,135.85,163.75,1.28
20260819,146,151,144.5,145,1961724,143.74,0.88,136.4,162.32,0.56
20260820,147,157,144.5,156.5,4598590,144.8,8.08,137.5,161.01,1.27
20260821,159,160,150,150.5,6080444,145.28,3.59,138.07,159.83,1.73
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 21.19
- over_600_ratio: 18.28
- over_800_ratio: 12.93
- over_1000_ratio: 9.71
- over_400_change_1w: 1.04
- over_800_change_1w: 1.12
- over_1000_change_1w: -1.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,16.15,-0.66,11.79,3.09,8.7,0,2,False,True
20260612,17.15,1,11.85,0.06,8.7,0,3,False,True
20260618,19.27,2.12,10.73,-1.12,10.73,2.03,4,False,True
20260626,19.23,-0.04,14.09,3.36,10.73,0,5,False,True
20260703,19.44,0.21,14.16,0.07,12.16,1.43,6,True,True
20260709,19.01,-0.43,12.94,-1.22,10.73,-1.43,0,False,False
20260717,22.82,3.81,13.46,0.52,12.4,1.67,1,True,True
20260724,22.09,-0.73,12.96,-0.5,10.73,-1.67,0,False,False
20260731,19.88,-2.21,12.77,-0.19,10.73,0,0,False,False
20260807,19.39,-0.49,12.84,0.07,10.73,0,1,False,True
20260814,20.15,0.76,11.81,-1.03,10.73,0,2,False,False
20260821,21.19,1.04,12.93,1.12,9.71,-1.02,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4977 | 眾達-KY | pattern | 型態觀察 | 47.0 |  |  | platform_right_side |  | call_inflow | stale_signal | 1.事實發生日:115/08/20 2.背書保證餘額達該公開發行公司最近期財務報表淨值百分之五十以上者: (1)被背書保證之公司名稱:PCL TECHNOLOGIES TRADING, INC. (2)與提供背書保證公司之關係: 本公司100%持股之子公司。 (3)迄事實發生日為止背書保證原因: 短期綜合額度及金融交易額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):419,384 (6)迄事實發生日為止背書保證餘額(仟元):586,750 (7)被背書保證公司實際動支金額(仟元):27,367 (8)本次新增背書保證之金額(仟元):167,366 (9)本次新增背書保證之原因: 短期綜合額度及金融交易額度續約(遠東銀行)。 (1)被背書保證之公司名稱:眾達光電股份有限公司 (2)與提供背書保證公司之關係: 本公司100%持股之子公司。 (3)迄事實發生日為止背書保證原因: 短期放款額度及聯貸授信額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):1,139,000 (6)迄事實發生日為止背書保證餘額(仟元):1,229,000 (7)被背書保證公司實際動支金額(仟元):1,009,000 (8)本次新增背書保證之金額(仟元):90,000 (9)本次新增背書保證之原因: 短期放款額度年度續約(遠東銀行)。 (1)被背書保證之公司名稱:眾達光通科技股份有限公司 (2)與提供背書保證公司之關係: 本公司100%持股之孫公司。 (3)迄事實發生日為止背書保證原因: 短期放款額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):90,000 (6)迄事實發生日為止背書保證餘額(仟元):180,000 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之金額(仟元):90,000 (9)本次新增背書保證之原因: 短期放款額度年度續約(遠東銀行)。 (1)被背書保證之公司名稱:PCL INTERNATIONAL TECHNOLOGIES (PENANG) SDN. BHD. (2)與提供背書保證公司之關係: 本公司100%持股之孫公司。 (3)迄事實發生日為止背書保證原因: 廠房貸款額度及營運週轉額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):0 (6)迄事實發生日為止背書保證餘額(仟元):608,546 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之金額(仟元):608,546 (9)本次新增背書保證之原因: 廠房貸款額度及營運週轉額度信用保證(Maybank Islamic Berhad)。 2.背書保證之總限額(仟元): 7,780,500 3.迄事實發生日為止，背書保證餘額(仟元): 4,430,296 3.迄事實發生日為止，提供背書保證餘額占公開發行公司最近期財務報表淨值之比 率: 113.88 4.其他應敘明事項: 美金匯率以1:32.31折算為新台幣。；calendar event: ex_right on 20260901; status=confirmed; proximity=within_14d |
| 20260821 | 4977 | 眾達-KY | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 46 | D_降級_TDCC轉弱 |  |  | call_inflow | stale_signal | 1.事實發生日:115/08/20 2.背書保證餘額達該公開發行公司最近期財務報表淨值百分之五十以上者: (1)被背書保證之公司名稱:PCL TECHNOLOGIES TRADING, INC. (2)與提供背書保證公司之關係: 本公司100%持股之子公司。 (3)迄事實發生日為止背書保證原因: 短期綜合額度及金融交易額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):419,384 (6)迄事實發生日為止背書保證餘額(仟元):586,750 (7)被背書保證公司實際動支金額(仟元):27,367 (8)本次新增背書保證之金額(仟元):167,366 (9)本次新增背書保證之原因: 短期綜合額度及金融交易額度續約(遠東銀行)。 (1)被背書保證之公司名稱:眾達光電股份有限公司 (2)與提供背書保證公司之關係: 本公司100%持股之子公司。 (3)迄事實發生日為止背書保證原因: 短期放款額度及聯貸授信額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):1,139,000 (6)迄事實發生日為止背書保證餘額(仟元):1,229,000 (7)被背書保證公司實際動支金額(仟元):1,009,000 (8)本次新增背書保證之金額(仟元):90,000 (9)本次新增背書保證之原因: 短期放款額度年度續約(遠東銀行)。 (1)被背書保證之公司名稱:眾達光通科技股份有限公司 (2)與提供背書保證公司之關係: 本公司100%持股之孫公司。 (3)迄事實發生日為止背書保證原因: 短期放款額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):90,000 (6)迄事實發生日為止背書保證餘額(仟元):180,000 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之金額(仟元):90,000 (9)本次新增背書保證之原因: 短期放款額度年度續約(遠東銀行)。 (1)被背書保證之公司名稱:PCL INTERNATIONAL TECHNOLOGIES (PENANG) SDN. BHD. (2)與提供背書保證公司之關係: 本公司100%持股之孫公司。 (3)迄事實發生日為止背書保證原因: 廠房貸款額度及營運週轉額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):0 (6)迄事實發生日為止背書保證餘額(仟元):608,546 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之金額(仟元):608,546 (9)本次新增背書保證之原因: 廠房貸款額度及營運週轉額度信用保證(Maybank Islamic Berhad)。 2.背書保證之總限額(仟元): 7,780,500 3.迄事實發生日為止，背書保證餘額(仟元): 4,430,296 3.迄事實發生日為止，提供背書保證餘額占公開發行公司最近期財務報表淨值之比 率: 113.88 4.其他應敘明事項: 美金匯率以1:32.31折算為新台幣。；calendar event: ex_right on 20260901; status=confirmed; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4977 | 眾達-KY | 3 | 1 | 3 | 3 | 3 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4977 | 眾達-KY | 109 | 6 | 9993600.0 | 1380.0 | 7241.74 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
