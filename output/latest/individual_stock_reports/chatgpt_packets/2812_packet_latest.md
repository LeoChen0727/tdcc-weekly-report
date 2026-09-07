# INDIVIDUAL STOCK CHATGPT PACKET - 2812 台中銀

## Metadata
- generated_at: 2026-09-06 22:16:38 Asia/Taipei
- stock_id: 2812
- stock_name: 台中銀
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2812_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2812_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2812_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2812_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2812_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2812_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2812_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2812_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2812_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2812_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2812_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2812_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2812.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2812.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2812.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2812.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2812_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2812_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2812_latest.md?ref=main

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
- date: 20260904
- open: 19.5
- high: 19.5
- low: 19.2
- close: 19.35
- volume: 9780826
- ma5: 19.27
- ema23_primary: 19.19
- distance_to_ema23_pct: 0.82
- ma20: 18.93
- ma60: 19.7
- ma120: 19.79
- return_5d: 2.65
- return_20d: 3.75
- volume_ratio: 0.76
- distance_to_ma20_pct_auxiliary: 2.21
- distance_to_high_60_pct: -7.19

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,18.7,18.75,18.4,18.7,14204737,19.81,-5.61,20.06,19.7,0.59
20260811,18.75,18.75,18.5,18.5,11664205,19.7,-6.1,19.96,19.7,0.49
20260812,18.55,18.75,18.45,18.65,10512480,19.61,-4.91,19.88,19.69,0.44
20260813,18.75,18.75,18.55,18.65,9215637,19.53,-4.52,19.8,19.68,0.39
20260814,18.55,18.7,18.5,18.65,10603928,19.46,-4.16,19.7,19.68,0.47
20260817,18.65,18.8,18.45,18.8,14695388,19.41,-3.12,19.63,19.68,0.67
20260818,18.7,19.05,18.7,19,13824159,19.37,-1.92,19.55,19.68,0.66
20260819,18.95,19,18.75,19,5671171,19.34,-1.76,19.48,19.68,0.28
20260820,19,19,18.75,18.8,6142878,19.3,-2.57,19.4,19.68,0.31
20260821,18.8,18.95,18.7,18.85,8506180,19.26,-2.12,19.32,19.68,0.43
20260824,18.85,19.1,18.8,19.05,11363006,19.24,-0.99,19.23,19.69,0.61
20260825,19.05,19.1,18.95,18.95,7161447,19.22,-1.39,19.14,19.7,0.41
20260826,18.95,19.05,18.85,19,7003880,19.2,-1.03,19.06,19.71,0.43
20260827,19,19.1,18.85,18.85,10026688,19.17,-1.67,18.97,19.71,0.64
20260828,19,19,18.75,18.85,7174322,19.14,-1.53,18.89,19.7,0.51
20260831,18.8,19.05,18.75,19.05,13658848,19.14,-0.44,18.81,19.7,1.04
20260901,18.9,19.1,18.9,19.1,23179162,19.13,-0.17,18.82,19.7,1.9
20260902,19.1,19.45,19.05,19.4,36663547,19.15,1.28,18.85,19.7,2.78
20260903,19.45,19.7,19.4,19.45,26875345,19.18,1.41,18.9,19.7,2.06
20260904,19.5,19.5,19.2,19.35,9780826,19.19,0.82,18.93,19.7,0.76
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 58.75
- over_600_ratio: 56.16
- over_800_ratio: 54.69
- over_1000_ratio: 53.75
- over_400_change_1w: 0.01
- over_800_change_1w: -0.02
- over_1000_change_1w: 0.05
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,58.57,0.02,54.46,-0.02,53.4,-0.03,1,False,False
20260626,58.87,0.3,54.73,0.27,53.7,0.3,2,True,True
20260703,58.87,0,54.78,0.05,53.77,0.07,3,False,True
20260709,59.15,0.28,55.02,0.24,54.03,0.26,4,True,True
20260717,59.22,0.07,55.04,0.02,54.08,0.05,5,True,True
20260724,59.3,0.08,55.08,0.04,54.13,0.05,6,True,True
20260731,59.53,0.23,55.42,0.34,54.54,0.41,7,True,True
20260807,58.78,-0.75,54.74,-0.68,53.78,-0.76,0,False,False
20260814,58.7,-0.08,54.65,-0.09,53.62,-0.16,0,False,False
20260821,58.7,0,54.72,0.07,53.67,0.05,1,False,True
20260828,58.74,0.04,54.71,-0.01,53.7,0.03,2,False,True
20260904,58.75,0.01,54.69,-0.02,53.75,0.05,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2812 | 台中銀 | pattern | 型態觀察 | 51.0 |  |  | base_building |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除權息 3.普通股發放股利種類及金額: 股票股利新臺幣4,034,489,370元，每股配發新臺幣0.67元。 現金股利新臺幣2,348,434,109元，每股配發新臺幣0.39元。 4.除權（息）交易日:115/08/04 5.最後過戶日:115/08/05 6.停止過戶起始日期:115/08/06 7.停止過戶截止日期:115/08/10 8.除權（息）基準日:115/08/10 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/09/09 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項: (1)股票股利於向經濟部完成變更登記後30日內，委由集保結算所以無實體方式直接    撥入股東之集保帳戶，屆時除另行公告外並分函通知股東。 (2)本次股利發放通知，另委託集保結算所辦理以電子化通知。請股東於除權（息）    停止過戶起始日一營業日前(即115年8月5日前)，逕登入集保結算所「股東e服務」    (網址 https://stockservices.tdcc.com.tw)之股務電子通知(eNotice)平台登記    同意接收電子通知，即可以留存之email接收股利發放通知。(115年8月6日以後同    意者，適用下次股利發放電子通知)；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2812 | 台中銀 | 5 | 1 | 5 | 5 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
