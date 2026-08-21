# INDIVIDUAL STOCK CHATGPT PACKET - 3176 基亞

## Metadata
- generated_at: 2026-08-21 22:27:16 Asia/Taipei
- stock_id: 3176
- stock_name: 基亞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3176_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3176_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3176_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3176_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3176_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3176_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3176_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3176_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3176_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3176_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3176_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3176_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3176.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3176.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3176.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3176.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3176_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3176_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3176_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
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
- open: 36
- high: 37.75
- low: 35.75
- close: 37.2
- volume: 1835000
- ma5: 35.17
- ema23_primary: 34.09
- distance_to_ema23_pct: 9.13
- ma20: 33.39
- ma60: 33.74
- ma120: 33.06
- return_5d: 10.22
- return_20d: 12.73
- volume_ratio: 3.5
- distance_to_ma20_pct_auxiliary: 11.41
- distance_to_high_60_pct: -5.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,32.85,33.4,32.75,33.4,232000,34.35,-2.76,34.91,34.04,0.33
20260728,33.35,33.35,32.35,32.35,297000,34.18,-5.36,34.87,34.03,0.42
20260729,32.75,32.8,31.7,32.05,399000,34,-5.75,34.79,34.01,0.58
20260730,32.05,32.05,31.1,31.1,227000,33.76,-7.88,34.65,33.97,0.34
20260731,31.7,31.75,31.15,31.15,226000,33.54,-7.14,34.51,33.94,0.34
20260803,31,31.9,31,31.65,149000,33.39,-5.2,34.32,33.92,0.25
20260804,31.45,31.95,31.45,31.65,628000,33.24,-4.79,34.05,33.89,1.18
20260805,32.8,34,32.65,33.5,1221000,33.26,0.71,33.81,33.91,2.46
20260806,33.8,34.35,32.3,32.45,965000,33.2,-2.25,33.55,33.92,2.05
20260807,32.5,33.75,32.2,33.7,309000,33.24,1.39,33.33,33.96,0.69
20260810,34.2,34.4,33.3,33.9,310000,33.29,1.82,33.23,34.01,0.76
20260811,33.9,34.05,33.1,33.45,383000,33.31,0.43,33.17,34,0.97
20260812,33.9,33.9,33.05,33.7,221000,33.34,1.08,33.08,33.95,0.57
20260813,33.9,34.6,33.7,34.15,422000,33.41,2.23,33,33.93,1.07
20260814,34.2,34.65,33.55,33.75,448000,33.44,0.94,33.01,33.87,1.16
20260817,33.95,34.45,33.8,34.15,493000,33.49,1.96,33.03,33.78,1.25
20260818,34.15,35.5,34.05,34.95,532000,33.62,3.97,33.09,33.74,1.31
20260819,34.6,34.8,34,34,310000,33.65,1.05,33.08,33.71,0.75
20260820,34.95,36.9,34.95,35.55,870000,33.81,5.16,33.18,33.7,1.96
20260821,36,37.75,35.75,37.2,1835000,34.09,9.13,33.39,33.74,3.5
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 35.22
- over_600_ratio: 30.98
- over_800_ratio: 29.08
- over_1000_ratio: 27.74
- over_400_change_1w: 0.83
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,34.58,-0.41,30.14,-0.46,29.45,0.16,4,False,True
20260605,34.46,-0.12,30.61,0.47,28.65,-0.8,5,False,True
20260612,34.46,0,29.75,-0.86,28.45,-0.2,0,False,False
20260618,34.26,-0.2,30.39,0.64,28.45,0,1,False,True
20260626,33.86,-0.4,30.4,0.01,28.46,0.01,2,False,True
20260703,33.91,0.05,30.45,0.05,28.5,0.04,3,True,True
20260709,35.12,1.21,30.51,0.06,28.56,0.06,4,True,True
20260717,35.35,0.23,30.62,0.11,28.67,0.11,5,True,True
20260724,34.34,-1.01,30.6,-0.02,28.67,0,0,False,False
20260731,34.62,0.28,30.04,-0.56,28.7,0.03,1,False,True
20260807,34.39,-0.23,29.07,-0.97,27.73,-0.97,0,False,False
20260814,35.22,0.83,29.08,0.01,27.74,0.01,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3176 | 基亞 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/06 2.契約或承諾相對人:Adara Bio Pty Ltd 3.與公司關係:子公司 4.契約或承諾起迄日期（或解除日期）:待合約簽訂日 5.主要內容（解除者不適用）:  本公司之重要子公司Medic Vision AI Limited(以下稱”MVA”)今日  (115/07/06)全體董事決議與Adara Bio Pty Ltd簽訂認股協議書(Subscription   Agreement)及股東契約(Shareholders Deed)，說明如下:  (1)Adara Bio Pty Ltd 為MVA與澳洲眼科中心(Centre for Eye Research     Australia Limited, CERA)合資設立的新公司。  (2)Adara Bio Pty Ltd將開發以 CRISPR 技術驅動之 RNA 鹼基對編輯療法，     用於治療眼部遺傳性疾病。  (3)MVA分兩期投資，於Adara Bio Pty Ltd達成里程碑，且MVA匯入第二期投     資款後取得50%股權。 6.限制條款（解除者不適用）:無 7.承諾事項（解除者不適用）:無 8.其他重要約定事項（解除者不適用）:無 9.對公司財務、業務之影響:對子公司財務及業務尚未產生重大影響。 10.具體目的:取得基因治療技術，強化子公司於眼科醫藥領域之佈局。 11.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項):  (1)新藥開發時程長、投入經費高且並未保證一定能成功，此等可能使投資  面臨風險，投資人應審慎判斷謹慎投資。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3176 | 基亞 | 1 | 1 | 1 | 2 | 6 | repeated_but_no_breakout | 近 10 日上榜 2 次、近 20 日上榜 6 次，但尚未有效突破，需等待攻擊確認。 |

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
