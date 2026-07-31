# INDIVIDUAL STOCK CHATGPT PACKET - 3479 安勤

## Metadata
- generated_at: 2026-07-31 22:27:13 Asia/Taipei
- stock_id: 3479
- stock_name: 安勤
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260724-88f3a903b384007d
- official_tdcc_signal_date: 20260724
- latest_tdcc_date: 20260724
- tdcc_rows: 13
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3479_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3479_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3479_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3479_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3479_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3479_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3479_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3479_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3479_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3479_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3479_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3479_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3479.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3479.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3479.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3479.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3479_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3479_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3479_latest.md?ref=main

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
- open: 135
- high: 138
- low: 127
- close: 127
- volume: 2734000
- ma5: 141.7
- ema23_primary: 140.91
- distance_to_ema23_pct: -9.87
- ma20: 143.05
- ma60: 130.17
- ma120: 109.92
- return_5d: -17.26
- return_20d: -8.96
- volume_ratio: 1
- distance_to_ma20_pct_auxiliary: -11.22
- distance_to_high_60_pct: -21.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,138,146.5,137.5,146.5,2258000,133.52,9.72,134.25,113.92,1.12
20260703,142.5,145,142.5,143,1417000,134.31,6.47,134.95,114.86,0.68
20260706,145.5,148,143,143,1812000,135.04,5.9,135.65,115.79,0.84
20260707,144,145,134,135,1549000,135.03,-0.03,136.3,116.54,0.7
20260708,135,136.5,133,136.5,855000,135.16,0.99,136.85,117.31,0.39
20260709,142,148.5,139.5,146,4254000,136.06,7.31,137.62,118.22,1.95
20260713,147,148.5,141,142.5,2264000,136.6,4.32,138.15,119.08,1.05
20260714,142.5,143.5,136,142,1962000,137.05,3.61,138.6,119.92,0.9
20260715,145,148.5,143,147.5,3005000,137.92,6.95,139.4,120.84,1.34
20260716,147.5,151,146,146,2676000,138.59,5.35,140.4,121.72,1.15
20260717,142.5,145.5,136.5,137.5,2483000,138.5,-0.72,140.6,122.46,1.06
20260720,136.5,139.5,126.5,135,1375000,138.21,-2.32,140.53,123.14,0.6
20260721,135,148.5,135,148.5,3033000,139.07,6.78,141.2,124.08,1.27
20260722,152.5,162,149,150,8010000,139.98,7.16,142.05,125.05,2.92
20260723,151,157,149,153.5,4426000,141.1,8.78,142.95,126.09,1.54
20260724,154,157,151,156.5,3418000,142.39,9.91,143.57,127.16,1.24
20260727,154,155.5,145,147.5,2907000,142.81,3.28,143.82,128.11,1.11
20260728,141,144,137.5,138,1908000,142.41,-3.1,143.8,128.9,0.73
20260729,142,142,130,139.5,2394000,142.17,-1.88,143.68,129.66,0.9
20260730,135,138,127,127,2734000,140.91,-9.87,143.05,130.17,1
```

## Latest TDCC Snapshot
- as_of_date: 20260724
- over_400_ratio: 41.67
- over_600_ratio: 35.88
- over_800_ratio: 33.98
- over_1000_ratio: 30.51
- over_400_change_1w: 0.62
- over_800_change_1w: -0.69
- over_1000_change_1w: -0.69
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260508,44.66,0.63,36.07,0,33.72,0,1,False,False
20260515,45.16,0.5,36.07,0,33.72,0,2,False,False
20260522,43.92,-1.24,36.07,0,33.72,0,0,False,False
20260529,45.74,1.82,36.07,0,33.72,0,1,False,False
20260605,43.92,-1.82,36.07,0,33.72,0,0,False,False
20260612,44.13,0.21,36.9,0.83,33.44,-0.28,1,False,True
20260618,43.54,-0.59,36.9,0,33.44,0,0,False,False
20260626,44.1,0.56,36.88,-0.02,33.42,-0.02,1,False,False
20260703,43.8,-0.3,36.62,-0.26,33.17,-0.25,0,False,False
20260709,42.64,-1.16,36.24,-0.38,32.76,-0.41,0,False,False
20260717,41.05,-1.59,34.67,-1.57,31.2,-1.56,0,False,False
20260724,41.67,0.62,33.98,-0.69,30.51,-0.69,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3479 | 安勤 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/03 2.公司名稱:安勤科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司股東會紀念品兌換條碼使用日期限制及因應辦法 6.因應措施: 本公司115年股東會開會通知書原載明，由電子投票平台領取之【全家便利商店中杯美式 咖啡兌換條碼 (下稱兌換條碼)】使用期限為118年6月30日。 惟因電子票券系統之設定限制，致該兌換條碼僅可使用至115年11月30日。若股東未及於 115年11月30日前兌換使用，請股東提供以下五項資訊寄至StockAffairs@avalue.com： 1.股東姓名 2.身分證字號或統一編號 3.聯絡電話 4.電子郵件 5.兌換條碼PIN序號(即QR碼下方顯示之PIN序號) 本公司將秉持維護股東權益的一貫立場協助後續處理，並確保股東的兌換使用權益至 118年6月30日 (即股東會開會通知書原載明兌換使用期限)。造成不便敬請見諒，並感謝 股東的理解與支持。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 3479 | 安勤 | revenue_pullback | 營收成長股價回檔 | 69.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/03 2.公司名稱:安勤科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司股東會紀念品兌換條碼使用日期限制及因應辦法 6.因應措施: 本公司115年股東會開會通知書原載明，由電子投票平台領取之【全家便利商店中杯美式 咖啡兌換條碼 (下稱兌換條碼)】使用期限為118年6月30日。 惟因電子票券系統之設定限制，致該兌換條碼僅可使用至115年11月30日。若股東未及於 115年11月30日前兌換使用，請股東提供以下五項資訊寄至StockAffairs@avalue.com： 1.股東姓名 2.身分證字號或統一編號 3.聯絡電話 4.電子郵件 5.兌換條碼PIN序號(即QR碼下方顯示之PIN序號) 本公司將秉持維護股東權益的一貫立場協助後續處理，並確保股東的兌換使用權益至 118年6月30日 (即股東會開會通知書原載明兌換使用期限)。造成不便敬請見諒，並感謝 股東的理解與支持。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3479 | 安勤 | 6 | 2 | 5 | 8 | 14 | repeated_but_no_breakout | 近 10 日上榜 8 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

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
