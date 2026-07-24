# INDIVIDUAL STOCK CHATGPT PACKET - 2887 台新新光金

## Metadata
- generated_at: 2026-07-24 22:26:55 Asia/Taipei
- stock_id: 2887
- stock_name: 台新新光金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2887_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2887_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2887_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2887_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2887_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2887_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2887_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2887_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2887_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2887_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2887_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2887_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2887.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2887.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2887.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2887.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2887_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2887_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2887_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260717
- open: 36
- high: 36
- low: 35.05
- close: 35.55
- volume: 96011039
- ma5: 35.81
- ema23_primary: 33.5
- distance_to_ema23_pct: 6.13
- ma20: 33.98
- ma60: 28.26
- ma120: 26.07
- return_5d: -3.53
- return_20d: 9.05
- volume_ratio: 1.24
- distance_to_ma20_pct_auxiliary: 4.61
- distance_to_high_60_pct: -5.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,32.95,33.55,32.1,32.45,109574168,28.13,15.35,27.53,25.16,0.7
20260622,32.6,32.6,31.95,32.05,62139229,28.46,12.62,27.94,25.29,0.4
20260623,32,32.95,32,32.15,74148243,28.77,11.77,28.39,25.42,0.49
20260624,32.05,32.15,31.6,31.6,59301672,29,8.96,28.79,25.54,0.4
20260625,31.6,32.3,31.6,31.85,49495606,29.24,8.93,29.21,25.67,0.35
20260626,31.75,32.15,31.3,31.9,52875362,29.46,8.28,29.66,25.81,0.39
20260629,32.4,33.3,32.1,33,84652109,29.76,10.9,30.14,25.97,0.66
20260630,33.45,33.5,32.8,33.25,79205481,30.05,10.66,30.57,26.13,0.65
20260701,33.5,34.1,32.75,33.35,91312723,30.32,9.99,30.93,26.28,0.8
20260702,33.3,33.8,32.95,33,51063157,30.55,8.04,31.17,26.42,0.5
20260703,32.95,34.9,32.95,34.15,108841693,30.85,10.71,31.45,26.58,1.15
20260706,34.15,34.8,34.15,34.3,34036658,31.13,10.17,31.73,26.74,0.38
20260707,34.3,35.5,34.3,34.9,85489406,31.45,10.98,32.09,26.91,0.98
20260708,35.45,36,35.2,35.85,77134233,31.81,12.68,32.41,27.11,0.91
20260709,36.45,37.15,36.3,36.85,111661117,32.23,14.32,32.8,27.31,1.32
20260713,37.3,37.75,35.6,35.75,86952795,32.53,9.91,33.16,27.5,1.02
20260714,36.15,36.15,34.4,35.45,87083713,32.77,8.18,33.42,27.67,1.06
20260715,36,36.8,35.5,36.15,78283271,33.05,9.37,33.65,27.87,0.98
20260716,36,36.3,35.45,36.15,65675402,33.31,8.52,33.84,28.07,0.85
20260717,36,36,35.05,35.55,96011039,33.5,6.13,33.98,28.26,1.24
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 74.86
- over_600_ratio: 72.99
- over_800_ratio: 71.76
- over_1000_ratio: 70.78
- over_400_change_1w: 0.04
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,73.12,,69.78,,68.76,,0,False,False
20260508,73.1,-0.02,69.75,-0.03,68.69,-0.07,0,False,False
20260515,72.95,-0.15,69.56,-0.19,68.52,-0.17,0,False,False
20260522,73.07,0.12,69.71,0.15,68.68,0.16,1,True,True
20260529,72.96,-0.11,69.56,-0.15,68.52,-0.16,0,False,False
20260605,73.7,0.74,70.41,0.85,69.4,0.88,1,True,True
20260612,73.93,0.23,70.68,0.27,69.67,0.27,2,True,True
20260618,74.37,0.44,71.18,0.5,70.19,0.52,3,True,True
20260626,74.41,0.04,71.2,0.02,70.21,0.02,4,True,True
20260703,74.62,0.21,71.44,0.24,70.45,0.24,5,True,True
20260709,74.82,0.2,71.65,0.21,70.68,0.23,6,True,True
20260717,74.86,0.04,71.76,0.11,70.78,0.1,7,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2887 | 台新新光金 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  | no_signal | stale_signal | 1.事實發生日:115/07/14 2.公司名稱:新光金國際創業投資股份有限公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:不適用 5.發生緣由: (1)台新創業投資股份有限公司（簡稱「台新創投」）與 新光金國際創業投資股份有限公司（簡稱「新光金創投」）於民國115年07月14日， 分別經其董事會(代行股東會)決議通過合併，並以台新創投為存續公司， 新光金創投為消滅公司（下稱「本合併案」），合併基準日暫定為115年09月01日。 (2)自合併基準日起，新光金創投之帳列資產、負債及一切權利義務， 均由台新創投概括承受。 6.因應措施: 謹依公司法第319條準用第73條及企業併購法第23條之規定辦理公告本合併案， 如債權人對本合併案有異議者，請於公告日起31日內，檢附債權證明文件， 以書面方式郵寄掛號（以郵戳日為憑）向新光金創投提出，逾期即視為無異議。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):無；calendar event: ex_right_dividend on 20260721; status=confirmed; proximity=within_3d |
| 20260717 | 2887 | 台新新光金 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/07/14 2.公司名稱:新光金國際創業投資股份有限公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:不適用 5.發生緣由: (1)台新創業投資股份有限公司（簡稱「台新創投」）與 新光金國際創業投資股份有限公司（簡稱「新光金創投」）於民國115年07月14日， 分別經其董事會(代行股東會)決議通過合併，並以台新創投為存續公司， 新光金創投為消滅公司（下稱「本合併案」），合併基準日暫定為115年09月01日。 (2)自合併基準日起，新光金創投之帳列資產、負債及一切權利義務， 均由台新創投概括承受。 6.因應措施: 謹依公司法第319條準用第73條及企業併購法第23條之規定辦理公告本合併案， 如債權人對本合併案有異議者，請於公告日起31日內，檢附債權證明文件， 以書面方式郵寄掛號（以郵戳日為憑）向新光金創投提出，逾期即視為無異議。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):無；calendar event: ex_right_dividend on 20260721; status=confirmed; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2887 | 台新新光金 | 4 | 4 | 4 | 9 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2887 | 台新新光金 | 29 | 0 | 2425980.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
