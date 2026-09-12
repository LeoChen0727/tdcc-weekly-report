# INDIVIDUAL STOCK CHATGPT PACKET - 5386 青雲

## Metadata
- generated_at: 2026-09-12 15:44:00 Asia/Taipei
- stock_id: 5386
- stock_name: 青雲
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 218
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5386_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5386_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5386.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5386.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5386.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5386.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5386_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5386_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5386_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: high_level_distribution_risk
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260911
- open: 327.5
- high: 339
- low: 312
- close: 318
- volume: 8779000
- ma5: 285.8
- ema23_primary: 272.2
- distance_to_ema23_pct: 16.83
- ma20: 257.62
- ma60: 317.38
- ma120: 369.73
- return_5d: 23.02
- return_20d: 22.07
- volume_ratio: 5.23
- distance_to_ma20_pct_auxiliary: 23.44
- distance_to_high_60_pct: -42.18

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,260.5,261,236.5,238.5,1491000,285.04,-16.33,253.38,403.74,1.31
20260818,238.5,246,227.5,228.5,1093000,280.33,-18.49,251.88,399.27,0.96
20260819,224,239,223,230.5,833000,276.18,-16.54,250.12,394.01,0.76
20260820,236.5,238,226.5,230.5,627000,272.37,-15.37,248.97,388.7,0.58
20260821,233,243.5,233,236,1374000,269.34,-12.38,248.05,382.85,1.26
20260824,239,246,238,242,879000,267.06,-9.38,247.75,377.3,0.8
20260825,240,241,228.5,236,753000,264.47,-10.77,248.38,371.35,0.69
20260826,238.5,241.5,234,234,571000,261.93,-10.66,249.38,365.57,0.54
20260827,234,237.5,233,235,582000,259.69,-9.51,250.78,360.17,0.57
20260828,237,258.5,237,258.5,2550000,259.59,-0.42,252.32,355.36,2.32
20260831,260,282.5,260,280,3699000,261.29,7.16,254.32,351.01,3
20260901,284,284.5,273,277.5,1701000,262.64,5.66,255.78,347.12,1.35
20260902,277.5,284.5,277,278,1437000,263.92,5.33,256.8,343.33,1.12
20260903,283,291,257,260,1768000,263.59,-1.36,256.25,338.53,1.34
20260904,263.5,266.5,252,258.5,853000,263.17,-1.77,255.62,334.59,0.65
20260907,260.5,265,259.5,259.5,558000,262.86,-1.28,253.7,330.87,0.44
20260908,259.5,264.5,257.5,257.5,466000,262.42,-1.87,252.85,327.07,0.39
20260909,283,283,283,283,671000,264.13,7.14,253.1,323.54,0.56
20260910,309.5,311,304,311,2883000,268.04,16.03,254.75,320.41,2.2
20260911,327.5,339,312,318,8779000,272.2,16.83,257.62,317.38,5.23
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 37.91
- over_600_ratio: 35.14
- over_800_ratio: 34.03
- over_1000_ratio: 32.37
- over_400_change_1w: 0.96
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,35.61,-0.06,30.78,0,28.28,0,0,False,False
20260703,36.66,1.05,30.78,0,28.28,0,1,False,False
20260709,36.98,0.32,30.78,0,28.28,0,2,False,False
20260717,37.53,0.55,30.78,0,28.28,0,3,False,False
20260724,34.31,-3.22,30.78,0,28.28,0,0,False,False
20260731,34.31,0,30.78,0,28.28,0,0,False,False
20260807,34.31,0,30.78,0,28.28,0,0,False,False
20260814,35.78,1.47,34.03,3.25,32.37,4.09,1,True,True
20260821,35.75,-0.03,34.03,0,32.37,0,0,False,False
20260828,35.67,-0.08,34.03,0,32.37,0,0,False,False
20260904,36.95,1.28,34.03,0,32.37,0,1,False,False
20260911,37.91,0.96,34.03,0,32.37,0,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 5386 | 青雲 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | continued_overheated | 1.董事會通過日期(事實發生日):115/09/09 2.舊會計師事務所名稱:眾智聯合會計師事務所 3.舊任簽證會計師姓名1: 楊永成 4.舊任簽證會計師姓名2: 謝佩芳 5.新會計師事務所名稱:富鋒聯合會計師事務所 6.新任簽證會計師姓名1: 吳金地 7.新任簽證會計師姓名2: 鄭忠昊 8.變更會計師之原因: 公司營運發展及整體管理需要 9.說明係由公司主動終止委任或不再繼續委任或前任會計師主動終止委任 或不再繼續接受委任: 公司主動不再繼續委任 10.公司通知或接獲通知終止之日期:115/09/09 11.最近二年度已申報或即將編製之財務報告是否曾經會計師調整或提出內 部控制重大改進事項之建議: 配合檢調單位調查客戶將高階伺服器銷售至中國大陸調查案件出具內部控制建議書 12.公司對上開調整或建議事項有無不同意見(若有不同意見，請詳細說明每 一事項之性質、公司原處理方法與最後處理結果暨繼任會計師對各該事 項之書面意見): 無 13.公司正式委任繼任會計師前，是否曾就上開前任會計師所做調整及建議 事項之處理及其對財務報表可能簽發之意見，諮詢該會計師(若有，請輸 入詢問事項及結果): 無 14.說明是否授權前任會計師對繼任會計師所提合理之詢問(包括上開所述不 同意見之情事)充分回答: 是 15.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則 重大訊息同時符合證券交易法施行細則第7條第7款所定對股東權益或 證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260911 | 5386 | 青雲 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | continued_overheated | 1.董事會通過日期(事實發生日):115/09/09 2.舊會計師事務所名稱:眾智聯合會計師事務所 3.舊任簽證會計師姓名1: 楊永成 4.舊任簽證會計師姓名2: 謝佩芳 5.新會計師事務所名稱:富鋒聯合會計師事務所 6.新任簽證會計師姓名1: 吳金地 7.新任簽證會計師姓名2: 鄭忠昊 8.變更會計師之原因: 公司營運發展及整體管理需要 9.說明係由公司主動終止委任或不再繼續委任或前任會計師主動終止委任 或不再繼續接受委任: 公司主動不再繼續委任 10.公司通知或接獲通知終止之日期:115/09/09 11.最近二年度已申報或即將編製之財務報告是否曾經會計師調整或提出內 部控制重大改進事項之建議: 配合檢調單位調查客戶將高階伺服器銷售至中國大陸調查案件出具內部控制建議書 12.公司對上開調整或建議事項有無不同意見(若有不同意見，請詳細說明每 一事項之性質、公司原處理方法與最後處理結果暨繼任會計師對各該事 項之書面意見): 無 13.公司正式委任繼任會計師前，是否曾就上開前任會計師所做調整及建議 事項之處理及其對財務報表可能簽發之意見，諮詢該會計師(若有，請輸 入詢問事項及結果): 無 14.說明是否授權前任會計師對繼任會計師所提合理之詢問(包括上開所述不 同意見之情事)充分回答: 是 15.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則 重大訊息同時符合證券交易法施行細則第7條第7款所定對股東權益或 證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 5386 | 青雲 | 2 | 2 | 2 | 4 | 9 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
