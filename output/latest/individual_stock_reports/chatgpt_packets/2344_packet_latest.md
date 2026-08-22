# INDIVIDUAL STOCK CHATGPT PACKET - 2344 華邦電

## Metadata
- generated_at: 2026-08-22 15:59:43 Asia/Taipei
- stock_id: 2344
- stock_name: 華邦電
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2344_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2344_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2344_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2344_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2344.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2344.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2344.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2344.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2344_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2344_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2344_latest.md?ref=main

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
- date: 20260821
- open: 176
- high: 182
- low: 174.5
- close: 181
- volume: 114128808
- ma5: 176.7
- ema23_primary: 169.97
- distance_to_ema23_pct: 6.49
- ma20: 163.22
- ma60: 173.28
- ma120: 139.77
- return_5d: -1.36
- return_20d: 17.15
- volume_ratio: 0.76
- distance_to_ma20_pct_auxiliary: 10.89
- distance_to_high_60_pct: -22.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,155,161,150,160,110420180,169.66,-5.7,173.12,159.28,0.77
20260728,144,147,144,144,69129108,167.52,-14.04,170.18,160.19,0.49
20260729,137,137.5,130,130,86091045,164.4,-20.92,166.3,160.76,0.65
20260730,123.5,133,117,118.5,208317971,160.57,-26.2,162.72,161.09,1.58
20260731,130,130,130,130,21043331,158.03,-17.73,160.05,161.45,0.17
20260803,134,143,133.5,143,77515412,156.77,-8.79,157.97,161.93,0.64
20260804,145,157,144,157,121631665,156.79,0.13,156.68,162.77,1.02
20260805,167,172.5,164.5,169,232656923,157.81,7.09,156.43,163.62,1.88
20260806,165.5,173,162,171,185766803,158.91,7.61,156.55,164.45,1.48
20260807,170,170.5,160.5,163.5,176709453,159.29,2.64,155.9,165.14,1.4
20260810,169,179.5,168.5,179.5,154758322,160.98,11.51,156.53,165.9,1.22
20260811,178,181,172.5,178,194693938,162.39,9.61,157.2,166.71,1.5
20260812,186.5,193,174.5,177,207363846,163.61,8.18,157.03,167.48,1.53
20260813,183,185,177,177,227421621,164.73,7.45,157.28,168.47,1.63
20260814,183,191,180.5,183.5,241145687,166.29,10.35,158.7,169.61,1.65
20260817,185.5,190,181.5,181.5,128521974,167.56,8.32,160.22,170.73,0.87
20260818,186,192,176,176.5,183343610,168.3,4.87,161.28,171.59,1.22
20260819,167,169.5,165,168,113062347,168.28,-0.17,161.12,172.25,0.75
20260820,174,180.5,172,176.5,149809828,168.96,4.46,161.9,172.84,0.99
20260821,176,182,174.5,181,114128808,169.97,6.49,163.22,173.28,0.76
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 69.68
- over_600_ratio: 68.4
- over_800_ratio: 67.51
- over_1000_ratio: 66.79
- over_400_change_1w: 0.72
- over_800_change_1w: 0.72
- over_1000_change_1w: 0.72
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,73.98,-0.05,71.71,-0.16,71.05,-0.08,0,False,False
20260612,71.59,-2.39,69.2,-2.51,68.57,-2.48,0,False,False
20260618,74.46,2.87,72.13,2.93,71.35,2.78,1,True,True
20260626,73.41,-1.05,71.04,-1.09,70.33,-1.02,0,False,False
20260703,71.18,-2.23,68.86,-2.18,68.12,-2.21,0,False,False
20260709,69.89,-1.29,67.69,-1.17,66.93,-1.19,0,False,False
20260717,69.81,-0.08,67.58,-0.11,66.74,-0.19,0,False,False
20260724,69.39,-0.42,67.14,-0.44,66.39,-0.35,0,False,False
20260731,68.57,-0.82,66.33,-0.81,65.63,-0.76,0,False,False
20260807,69.96,1.39,67.81,1.48,67.16,1.53,1,True,True
20260814,68.96,-1,66.79,-1.02,66.07,-1.09,0,False,False
20260821,69.68,0.72,67.51,0.72,66.79,0.72,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2344 | 華邦電 | pattern | 型態觀察 | 46.0 |  |  | base_building |  | no_signal | stale_signal | 1.事實發生日:115/07/13 2.公司名稱:華邦電子股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:依本公司海外第四次無擔保轉換公司債發行及轉換辦法第十二(一)條規定， 本債券發行之日起屆滿三個月之翌日至到期日前，如本公司普通股於台灣證券交易所之 收盤價格，連續三十個營業日中有二十個交易日(如遇除權或除息者，於除權或除息交 易日至除權或除息基準日之間，採用之收盤價格，應先設算為除權或除息前之價格)達 提前贖回金額(定義於後)除以本債券面額再乘以當時轉換價格後所得之總數120%時，本 公司得以提前贖回金額贖回全部或部份本債券。 「提前贖回金額」係指公司依本債券面額加計年利率為-1.5%之利息補償金，且以每半 年為計算基礎所得之金額。 提前贖回金額將按固定匯率換算為新臺幣，並以該新臺幣金額按贖回當時匯率(參考上 午十一時Taipei Forex Inc.所顯示之定盤匯率)換算為美金償還。 6.因應措施:本公司將於115年8月12日提前贖回全部海外第四次無擔保轉換公司債。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 2344 | 華邦電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/07/13 2.公司名稱:華邦電子股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:依本公司海外第四次無擔保轉換公司債發行及轉換辦法第十二(一)條規定， 本債券發行之日起屆滿三個月之翌日至到期日前，如本公司普通股於台灣證券交易所之 收盤價格，連續三十個營業日中有二十個交易日(如遇除權或除息者，於除權或除息交 易日至除權或除息基準日之間，採用之收盤價格，應先設算為除權或除息前之價格)達 提前贖回金額(定義於後)除以本債券面額再乘以當時轉換價格後所得之總數120%時，本 公司得以提前贖回金額贖回全部或部份本債券。 「提前贖回金額」係指公司依本債券面額加計年利率為-1.5%之利息補償金，且以每半 年為計算基礎所得之金額。 提前贖回金額將按固定匯率換算為新臺幣，並以該新臺幣金額按贖回當時匯率(參考上 午十一時Taipei Forex Inc.所顯示之定盤匯率)換算為美金償還。 6.因應措施:本公司將於115年8月12日提前贖回全部海外第四次無擔保轉換公司債。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2344 | 華邦電 | 18 | 3 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2344 | 華邦電 | 360 | 39 | 50395630.0 | 1717280.0 | 29.35 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
