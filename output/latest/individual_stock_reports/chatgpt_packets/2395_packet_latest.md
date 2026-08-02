# INDIVIDUAL STOCK CHATGPT PACKET - 2395 研華

## Metadata
- generated_at: 2026-08-02 22:26:40 Asia/Taipei
- stock_id: 2395
- stock_name: 研華
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 315
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2395_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2395_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2395_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2395_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2395_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2395_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2395_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2395_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2395_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2395_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2395_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2395_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2395.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2395.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2395.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2395.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2395_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2395_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2395_latest.md?ref=main

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
- date: 20260730
- open: 553
- high: 555
- low: 535
- close: 547
- volume: 4281013
- ma5: 562.2
- ema23_primary: 538.98
- distance_to_ema23_pct: 1.49
- ma20: 542.98
- ma60: 501.8
- ma120: 418.49
- return_5d: -8.83
- return_20d: 8.75
- volume_ratio: 1.09
- distance_to_ma20_pct_auxiliary: 0.74
- distance_to_high_60_pct: -11.49

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,493.5,511,493.5,510,1952536,483.02,5.59,485.1,443.38,0.64
20260703,498.5,522,498.5,521,2059910,486.19,7.16,485.05,446.26,0.7
20260706,523,528,506,515,1522169,488.59,5.41,486,449.04,0.55
20260707,519,522,493,496.5,1854906,489.25,1.48,487.27,451.55,0.7
20260708,546,546,533,546,8005111,493.98,10.53,490.1,454.94,2.82
20260709,547,562,537,540,6782199,497.81,8.47,493.82,458.21,2.26
20260713,557,593,535,536,4473042,500.99,6.99,497.43,461.34,1.49
20260714,552,553,508,529,2602857,503.33,5.1,500.23,464.24,0.84
20260715,530,539,526,533,1927304,505.8,5.38,502.62,467.02,0.63
20260716,530,531,520,530,2286309,507.82,4.37,505.12,469.8,0.74
20260717,518,519,502,513,2570650,508.25,0.93,506.35,472.27,0.83
20260720,519,521,493.5,516,3844639,508.89,1.4,507.45,474.86,1.24
20260721,525,567,519,567,4357157,513.74,10.37,510.82,478.37,1.38
20260722,589,618,584,596,9512024,520.59,14.48,516.25,482.4,2.71
20260723,605,607,582,600,3860896,527.21,13.81,522.58,486.35,1.08
20260724,585,616,578,581,4213688,531.69,9.27,527.62,489.92,1.14
20260727,586,588,557,577,3909996,535.47,7.76,533.7,493.43,1.03
20260728,555,570,547,556,3455170,537.18,3.5,537.88,496.71,0.93
20260729,549,565,529,550,5325464,538.25,2.18,540.77,499.29,1.38
20260730,553,555,535,547,4281013,538.98,1.49,542.98,501.8,1.09
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 85.65
- over_600_ratio: 82.14
- over_800_ratio: 80.21
- over_1000_ratio: 78.02
- over_400_change_1w: -0.04
- over_800_change_1w: 0.08
- over_1000_change_1w: -0.13
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,86.08,-0.23,80.91,-0.19,78.99,-0.14,0,False,False
20260522,85.93,-0.15,80.58,-0.33,78.35,-0.64,0,False,False
20260529,85.51,-0.42,80.23,-0.35,78.36,0.01,1,False,True
20260605,85.23,-0.28,79.55,-0.68,77.65,-0.71,0,False,False
20260612,85.03,-0.2,80,0.45,78,0.35,1,False,True
20260618,84.96,-0.07,79.87,-0.13,77.86,-0.14,0,False,False
20260626,85.1,0.14,79.94,0.07,77.77,-0.09,1,False,True
20260703,85.4,0.3,80.1,0.16,78.03,0.26,2,True,True
20260709,85.49,0.09,79.92,-0.18,77.94,-0.09,3,False,False
20260717,85.67,0.18,80.26,0.34,78.17,0.23,4,True,True
20260724,85.69,0.02,80.13,-0.13,78.15,-0.02,5,False,False
20260731,85.65,-0.04,80.21,0.08,78.02,-0.13,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2395 | 研華 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/08/05 1.召開法人說明會之日期：115/08/05 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：研華內湖辦公室(台北市內湖區瑞光路26巷20弄1號) 4.法人說明會擇要訊息：(1)公布本公司2026年第二季財務報告及2026年第三季業績展望。 (2)參加方式：請參見  https://advt.ch/2Q26-Investor-Conference 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2395 | 研華 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/08/05 1.召開法人說明會之日期：115/08/05 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：研華內湖辦公室(台北市內湖區瑞光路26巷20弄1號) 4.法人說明會擇要訊息：(1)公布本公司2026年第二季財務報告及2026年第三季業績展望。 (2)參加方式：請參見  https://advt.ch/2Q26-Investor-Conference 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2395 | 研華 | 26 | 2 | 5 | 10 | 20 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 20 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2395 | 研華 | 66 | 0 | 10881660.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
