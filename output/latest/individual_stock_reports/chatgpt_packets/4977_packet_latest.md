# INDIVIDUAL STOCK CHATGPT PACKET - 4977 眾達-KY

## Metadata
- generated_at: 2026-09-05 22:17:05 Asia/Taipei
- stock_id: 4977
- stock_name: 眾達-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 347
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: high_level_consolidation
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
- date: 20260904
- open: 177
- high: 185
- low: 172
- close: 185
- volume: 6114009
- ma5: 177.5
- ema23_primary: 161.01
- distance_to_ema23_pct: 14.9
- ma20: 160.15
- ma60: 154.38
- ma120: 181.48
- return_5d: 7.56
- return_20d: 38.58
- volume_ratio: 1.27
- distance_to_ma20_pct_auxiliary: 15.52
- distance_to_high_60_pct: -4.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
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
20260824,150,154,145,145,2354174,145.25,-0.17,138.65,158.74,0.69
20260825,144,157,142,155,3299223,146.07,6.12,140.2,157.82,0.97
20260826,156,170.5,155,170.5,7963102,148.1,15.12,143.12,157.04,2.15
20260827,175.5,181.5,171.5,171.5,10551960,150.05,14.29,146.38,156.36,2.57
20260828,171.5,177.5,170,172,3489659,151.88,13.25,149.12,155.57,0.83
20260831,171,176,168,175,3005963,153.81,13.78,151.8,155,0.71
20260901,179.5,184.5,178,178.5,6878283,155.87,14.52,154.18,154.63,1.55
20260902,176,189.5,175.5,176.5,6016083,157.59,12,155.88,154.57,1.35
20260903,179.5,186,171.5,172.5,6148309,158.83,8.61,157.57,154.23,1.34
20260904,177,185,172,185,6114009,161.01,14.9,160.15,154.38,1.27
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 19.2
- over_600_ratio: 15.17
- over_800_ratio: 11.6
- over_1000_ratio: 8.43
- over_400_change_1w: -1.88
- over_800_change_1w: -0.49
- over_1000_change_1w: -1.63
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
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
20260828,21.08,-0.11,12.09,-0.84,10.06,0.35,4,False,True
20260904,19.2,-1.88,11.6,-0.49,8.43,-1.63,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4977 | 眾達-KY | range_rebound | 區間內轉強 / 挑戰前高觀察 | 60.0 |  |  | neckline_challenge |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/08/20 2.背書保證餘額達該公開發行公司最近期財務報表淨值百分之五十以上者: (1)被背書保證之公司名稱:PCL TECHNOLOGIES TRADING, INC. (2)與提供背書保證公司之關係: 本公司100%持股之子公司。 (3)迄事實發生日為止背書保證原因: 短期綜合額度及金融交易額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):419,384 (6)迄事實發生日為止背書保證餘額(仟元):586,750 (7)被背書保證公司實際動支金額(仟元):27,367 (8)本次新增背書保證之金額(仟元):167,366 (9)本次新增背書保證之原因: 短期綜合額度及金融交易額度續約(遠東銀行)。 (1)被背書保證之公司名稱:眾達光電股份有限公司 (2)與提供背書保證公司之關係: 本公司100%持股之子公司。 (3)迄事實發生日為止背書保證原因: 短期放款額度及聯貸授信額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):1,139,000 (6)迄事實發生日為止背書保證餘額(仟元):1,229,000 (7)被背書保證公司實際動支金額(仟元):1,009,000 (8)本次新增背書保證之金額(仟元):90,000 (9)本次新增背書保證之原因: 短期放款額度年度續約(遠東銀行)。 (1)被背書保證之公司名稱:眾達光通科技股份有限公司 (2)與提供背書保證公司之關係: 本公司100%持股之孫公司。 (3)迄事實發生日為止背書保證原因: 短期放款額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):90,000 (6)迄事實發生日為止背書保證餘額(仟元):180,000 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之金額(仟元):90,000 (9)本次新增背書保證之原因: 短期放款額度年度續約(遠東銀行)。 (1)被背書保證之公司名稱:PCL INTERNATIONAL TECHNOLOGIES (PENANG) SDN. BHD. (2)與提供背書保證公司之關係: 本公司100%持股之孫公司。 (3)迄事實發生日為止背書保證原因: 廠房貸款額度及營運週轉額度信用保證。 (4)背書保證之限額(仟元):7,780,500 (5)原背書保證之餘額(仟元):0 (6)迄事實發生日為止背書保證餘額(仟元):608,546 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之金額(仟元):608,546 (9)本次新增背書保證之原因: 廠房貸款額度及營運週轉額度信用保證(Maybank Islamic Berhad)。 2.背書保證之總限額(仟元): 7,780,500 3.迄事實發生日為止，背書保證餘額(仟元): 4,430,296 3.迄事實發生日為止，提供背書保證餘額占公開發行公司最近期財務報表淨值之比 率: 113.88 4.其他應敘明事項: 美金匯率以1:32.31折算為新台幣。；calendar event: ex_right on 20260901; status=confirmed; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4977 | 眾達-KY | 1 | 1 | 1 | 3 | 5 | repeated_but_no_breakout | 近 10 日上榜 3 次、近 20 日上榜 5 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4977 | 眾達-KY | 117 | 7 | 15510890.0 | 15850.0 | 978.61 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
