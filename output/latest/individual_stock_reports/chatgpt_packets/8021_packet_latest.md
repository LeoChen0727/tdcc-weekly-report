# INDIVIDUAL STOCK CHATGPT PACKET - 8021 尖點

## Metadata
- generated_at: 2026-08-22 16:01:17 Asia/Taipei
- stock_id: 8021
- stock_name: 尖點
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8021_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8021_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8021_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8021_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8021.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8021.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8021.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8021.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8021_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8021_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8021_latest.md?ref=main

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
- open: 407
- high: 410.5
- low: 394
- close: 397
- volume: 3418276
- ma5: 407.1
- ema23_primary: 414.56
- distance_to_ema23_pct: -4.24
- ma20: 391.43
- ma60: 463.43
- ma120: 400.89
- return_5d: -8.53
- return_20d: 7.3
- volume_ratio: 0.72
- distance_to_ma20_pct_auxiliary: 1.42
- distance_to_high_60_pct: -36.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,372,390.5,360.5,390.5,6724084,465.1,-16.04,484.43,474.57,1.71
20260728,360,366,351.5,351.5,3342833,455.63,-22.85,475.9,473.73,0.83
20260729,346,349.5,316.5,316.5,2093691,444.04,-28.72,463.02,471.92,0.52
20260730,290.5,320,285,294,8605059,431.53,-31.87,449.68,469.71,2.27
20260731,323,323,323,323,619360,422.49,-23.55,438.62,468.02,0.19
20260803,331.5,355,330,355,3153592,416.87,-14.84,428.48,466.85,0.93
20260804,370,390.5,363.5,390.5,5308977,414.67,-5.83,421.5,466.68,1.47
20260805,429.5,429.5,392,396,11219384,413.11,-4.14,416.4,466.12,2.74
20260806,395.5,432,384.5,417.5,9987285,413.48,0.97,411.38,465.23,2.2
20260807,420,424,392,395,6925065,411.94,-4.11,405.07,464.38,1.43
20260810,408.5,434.5,408.5,434.5,6014329,413.82,5,401.4,463.44,1.17
20260811,424.5,444,414,439,1335242,415.92,5.55,398.98,463.4,0.26
20260812,439.5,441,421,427,1141530,416.84,2.44,393.73,463.84,0.22
20260813,439,446.5,427.5,429,1028740,417.85,2.67,389.93,464.46,0.2
20260814,431,437,415,434,1114375,419.2,3.53,388.9,465.68,0.22
20260817,423.5,431,395,428,1631315,419.93,1.92,389.82,466.41,0.32
20260818,437,452,400,408.5,10703530,418.98,-2.5,391.23,466.18,2.1
20260819,392,413,391,393.5,5308156,416.86,-5.6,389.98,465.01,1.03
20260820,402.5,418.5,401,408.5,4979209,416.16,-1.84,390.07,464.07,1
20260821,407,410.5,394,397,3418276,414.56,-4.24,391.43,463.43,0.72
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 45.88
- over_600_ratio: 41.24
- over_800_ratio: 38.87
- over_1000_ratio: 35.75
- over_400_change_1w: -1.22
- over_800_change_1w: -1.26
- over_1000_change_1w: -2.54
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,48.3,0.32,41.99,-0.8,38.39,-0.16,2,False,False
20260612,52.3,4,42.17,0.18,38.5,0.11,3,True,True
20260618,46.57,-5.73,37.98,-4.19,35.05,-3.45,0,False,False
20260626,47.84,1.27,40.38,2.4,37.38,2.33,1,True,True
20260703,47.91,0.07,40.61,0.23,37.17,-0.21,2,False,True
20260709,48.03,0.12,40.86,0.25,37.85,0.68,3,False,True
20260717,47.46,-0.57,40.91,0.05,37.93,0.08,4,False,True
20260724,46.23,-1.23,39.9,-1.01,36.93,-1,0,False,False
20260731,46.38,0.15,38.67,-1.23,33.85,-3.08,1,False,False
20260807,46.88,0.5,38.32,-0.35,35.82,1.97,2,False,True
20260814,47.1,0.22,40.13,1.81,38.29,2.47,3,True,True
20260821,45.88,-1.22,38.87,-1.26,35.75,-2.54,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8021 | 尖點 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/07/01 2.公司名稱:尖點科技股份有限公司。 3.與公司關係(請輸入本公司或子公司):本公司。 4.相互持股比例:不適用。 5.發生緣由:因應本公司配發普通股現金股利，依本公司國內第二次 無擔保轉換公司債發行及轉換辦法第十一條規定調整轉換價格。 6.因應措施:本公司因發行國內第二次私募無擔保轉換公司債， 已依本公司國內第二次無擔保轉換公司債發行及轉換辦法第十一 條規定，於115年6月24日將本公司國內第二次無擔保轉換公司債 之轉換價格由新台幣201.8元調整為201.1元；另因配發普通股現金 股利，自除息基準日（115年7月21日）起，再將轉換價格由新台幣 201.1元調整為200.4元。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 8021 | 尖點 | revenue_pullback | 營收成長股價回檔 | 50.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/01 2.公司名稱:尖點科技股份有限公司。 3.與公司關係(請輸入本公司或子公司):本公司。 4.相互持股比例:不適用。 5.發生緣由:因應本公司配發普通股現金股利，依本公司國內第二次 無擔保轉換公司債發行及轉換辦法第十一條規定調整轉換價格。 6.因應措施:本公司因發行國內第二次私募無擔保轉換公司債， 已依本公司國內第二次無擔保轉換公司債發行及轉換辦法第十一 條規定，於115年6月24日將本公司國內第二次無擔保轉換公司債 之轉換價格由新台幣201.8元調整為201.1元；另因配發普通股現金 股利，自除息基準日（115年7月21日）起，再將轉換價格由新台幣 201.1元調整為200.4元。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8021 | 尖點 | 4 | 4 | 4 | 5 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
