# INDIVIDUAL STOCK CHATGPT PACKET - 3479 安勤

## Metadata
- generated_at: 2026-09-26 15:51:58 Asia/Taipei
- stock_id: 3479
- stock_name: 安勤
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260924
- open: 130
- high: 136.5
- low: 130
- close: 136
- volume: 1272000
- ma5: 131.8
- ema23_primary: 130.54
- distance_to_ema23_pct: 4.18
- ma20: 128.7
- ma60: 135.17
- ma120: 124.03
- return_5d: 4.62
- return_20d: 5.43
- volume_ratio: 2.27
- distance_to_ma20_pct_auxiliary: 5.67
- distance_to_high_60_pct: -16.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,130,130.5,129,129,325000,133.34,-3.26,133.68,136.72,0.37
20260831,129,129,125.5,126.5,478000,132.77,-4.72,133.32,136.68,0.57
20260901,126,127,125,125.5,751000,132.17,-5.04,132.93,136.62,0.92
20260902,126,126.5,123.5,124,439000,131.49,-5.69,132.12,136.66,0.59
20260903,124,125,122,122,411000,130.7,-6.65,131.18,136.6,0.6
20260904,125,127.5,123.5,127,397000,130.39,-2.6,130.6,136.54,0.61
20260907,128,128,125,125.5,285000,129.98,-3.45,129.72,136.43,0.47
20260908,125.5,125.5,122,122.5,276000,129.36,-5.3,128.8,136.26,0.5
20260909,125.5,132.5,124,131.5,1495000,129.54,1.52,128.35,136.26,2.49
20260910,129.5,133.5,129.5,133,1164000,129.82,2.45,128.03,136.38,1.87
20260911,130.5,134,130,131,717000,129.92,0.83,128.1,136.33,1.39
20260914,129,132,128.5,129,298000,129.85,-0.65,128.07,136.21,0.59
20260915,132,133.5,129.5,129.5,372000,129.82,-0.24,128.18,136.12,0.74
20260916,131,131,129,129,238000,129.75,-0.58,128.07,136.05,0.48
20260917,130,132,129.5,130,423000,129.77,0.18,128.07,135.96,0.85
20260918,131.5,132.5,129.5,131.5,416000,129.91,1.22,128.28,135.75,0.84
20260921,132.5,134,130.5,131.5,470000,130.05,1.12,128.45,135.57,0.94
20260922,133.5,135,129.5,129.5,605000,130,-0.39,128.38,135.42,1.17
20260923,130.5,131.5,128,130.5,379000,130.04,0.35,128.35,135.22,0.74
20260924,130,136.5,130,136,1272000,130.54,4.18,128.7,135.17,2.27
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 39.82
- over_600_ratio: 34.53
- over_800_ratio: 32.62
- over_1000_ratio: 30.26
- over_400_change_1w: -0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,42.64,-1.16,36.24,-0.38,32.76,-0.41,0,False,False
20260717,41.05,-1.59,34.67,-1.57,31.2,-1.56,0,False,False
20260724,41.67,0.62,33.98,-0.69,30.51,-0.69,1,False,False
20260731,40.68,-0.99,32.74,-1.24,30.43,-0.08,0,False,False
20260807,40.3,-0.38,32.77,0.03,30.43,0,1,False,True
20260814,40.26,-0.04,32.61,-0.16,30.27,-0.16,0,False,False
20260821,40.33,0.07,32.61,0,30.27,0,1,False,False
20260828,40.35,0.02,32.61,0,30.27,0,2,False,False
20260904,40.37,0.02,32.61,0,30.27,0,3,False,False
20260911,39.82,-0.55,32.63,0.02,30.27,0,4,False,True
20260918,39.83,0.01,32.62,-0.01,30.26,-0.01,5,False,False
20260924,39.82,-0.01,32.62,0,30.26,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3479 | 安勤 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/03 2.公司名稱:安勤科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司股東會紀念品兌換條碼使用日期限制及因應辦法 6.因應措施: 本公司115年股東會開會通知書原載明，由電子投票平台領取之【全家便利商店中杯美式 咖啡兌換條碼 (下稱兌換條碼)】使用期限為118年6月30日。 惟因電子票券系統之設定限制，致該兌換條碼僅可使用至115年11月30日。若股東未及於 115年11月30日前兌換使用，請股東提供以下五項資訊寄至StockAffairs@avalue.com： 1.股東姓名 2.身分證字號或統一編號 3.聯絡電話 4.電子郵件 5.兌換條碼PIN序號(即QR碼下方顯示之PIN序號) 本公司將秉持維護股東權益的一貫立場協助後續處理，並確保股東的兌換使用權益至 118年6月30日 (即股東會開會通知書原載明兌換使用期限)。造成不便敬請見諒，並感謝 股東的理解與支持。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 3479 | 安勤 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/03 2.公司名稱:安勤科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司股東會紀念品兌換條碼使用日期限制及因應辦法 6.因應措施: 本公司115年股東會開會通知書原載明，由電子投票平台領取之【全家便利商店中杯美式 咖啡兌換條碼 (下稱兌換條碼)】使用期限為118年6月30日。 惟因電子票券系統之設定限制，致該兌換條碼僅可使用至115年11月30日。若股東未及於 115年11月30日前兌換使用，請股東提供以下五項資訊寄至StockAffairs@avalue.com： 1.股東姓名 2.身分證字號或統一編號 3.聯絡電話 4.電子郵件 5.兌換條碼PIN序號(即QR碼下方顯示之PIN序號) 本公司將秉持維護股東權益的一貫立場協助後續處理，並確保股東的兌換使用權益至 118年6月30日 (即股東會開會通知書原載明兌換使用期限)。造成不便敬請見諒，並感謝 股東的理解與支持。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 3479 | 安勤 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/03 2.公司名稱:安勤科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司股東會紀念品兌換條碼使用日期限制及因應辦法 6.因應措施: 本公司115年股東會開會通知書原載明，由電子投票平台領取之【全家便利商店中杯美式 咖啡兌換條碼 (下稱兌換條碼)】使用期限為118年6月30日。 惟因電子票券系統之設定限制，致該兌換條碼僅可使用至115年11月30日。若股東未及於 115年11月30日前兌換使用，請股東提供以下五項資訊寄至StockAffairs@avalue.com： 1.股東姓名 2.身分證字號或統一編號 3.聯絡電話 4.電子郵件 5.兌換條碼PIN序號(即QR碼下方顯示之PIN序號) 本公司將秉持維護股東權益的一貫立場協助後續處理，並確保股東的兌換使用權益至 118年6月30日 (即股東會開會通知書原載明兌換使用期限)。造成不便敬請見諒，並感謝 股東的理解與支持。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3479 | 安勤 | 1 | 1 | 1 | 3 | 3 | repeated_but_no_breakout | 近 10 日上榜 3 次、近 20 日上榜 3 次，但尚未有效突破，需等待攻擊確認。 |

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
