# INDIVIDUAL STOCK CHATGPT PACKET - 1102 亞泥

## Metadata
- generated_at: 2026-08-22 22:26:19 Asia/Taipei
- stock_id: 1102
- stock_name: 亞泥
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1102_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1102_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1102_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1102_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1102_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1102_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1102_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1102_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1102_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1102_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1102_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1102_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1102.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1102.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1102.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1102.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1102_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1102_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1102_latest.md?ref=main

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
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
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
- date: 20260821
- open: 34.7
- high: 35.05
- low: 34.6
- close: 34.95
- volume: 16339386
- ma5: 34.08
- ema23_primary: 33.49
- distance_to_ema23_pct: 4.37
- ma20: 33.09
- ma60: 34.16
- ma120: 34.52
- return_5d: 4.48
- return_20d: 6.72
- volume_ratio: 1.32
- distance_to_ma20_pct_auxiliary: 5.61
- distance_to_high_60_pct: -5.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,33.1,33.15,32.7,33.1,7626983,34.12,-3,34.5,34.63,0.36
20260728,33.1,33.25,32.75,33,7469256,34.03,-3.03,34.38,34.6,0.36
20260729,33.15,33.3,32.25,32.8,13231020,33.93,-3.32,34.27,34.56,0.65
20260730,33,33.4,32.75,33.2,11167397,33.87,-1.97,34.17,34.53,0.68
20260731,33.3,33.6,32.7,33,33282302,33.79,-2.35,34.01,34.5,1.97
20260803,32.65,32.8,32.35,32.7,11458827,33.7,-2.98,33.82,34.46,0.69
20260804,32.35,32.5,32.2,32.4,10095354,33.59,-3.56,33.61,34.42,0.61
20260805,32.4,32.6,32.25,32.6,8109403,33.51,-2.72,33.42,34.38,0.5
20260806,32.5,32.95,32.5,32.95,6106789,33.47,-1.54,33.28,34.36,0.38
20260807,32.8,33.05,32.8,32.85,4786576,33.41,-1.69,33.14,34.32,0.31
20260810,33,33,32.5,32.95,4654967,33.38,-1.27,33.04,34.28,0.31
20260811,32.85,33,32.35,32.45,8219126,33.3,-2.55,32.95,34.25,0.58
20260812,32.6,32.65,32.3,32.35,7111395,33.22,-2.62,32.83,34.21,0.54
20260813,32.55,32.55,31.6,31.7,19553836,33.09,-4.21,32.77,34.16,1.6
20260814,32.5,33.45,32.45,33.45,26219343,33.12,0.99,32.78,34.14,2.18
20260817,33.3,33.8,33.2,33.45,8435593,33.15,0.91,32.8,34.12,0.72
20260818,33.3,33.5,33.2,33.5,5619606,33.18,0.97,32.82,34.1,0.49
20260819,33.5,33.85,33.15,33.8,11995199,33.23,1.71,32.88,34.11,1.1
20260820,33.95,34.9,33.9,34.7,25215460,33.35,4.04,32.98,34.13,2.13
20260821,34.7,35.05,34.6,34.95,16339386,33.49,4.37,33.09,34.16,1.32
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 81.4
- over_600_ratio: 80.3
- over_800_ratio: 79.63
- over_1000_ratio: 79.12
- over_400_change_1w: 0.48
- over_800_change_1w: 0.6
- over_1000_change_1w: 0.54
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,81.23,0.04,79.4,0.37,79,0.64,1,True,True
20260612,81.17,-0.06,79.26,-0.14,78.86,-0.14,0,False,False
20260618,81.48,0.31,79.62,0.36,79.17,0.31,1,True,True
20260626,81.8,0.32,79.95,0.33,79.48,0.31,2,True,True
20260703,81.82,0.02,80.04,0.09,79.59,0.11,3,True,True
20260709,81.85,0.03,80.22,0.18,79.72,0.13,4,True,True
20260717,81.13,-0.72,79.41,-0.81,78.98,-0.74,0,False,False
20260724,81.13,0,79.34,-0.07,78.91,-0.07,0,False,False
20260731,81.43,0.3,79.64,0.3,79.19,0.28,1,True,True
20260807,81.35,-0.08,79.51,-0.13,79.11,-0.08,0,False,False
20260814,80.92,-0.43,79.03,-0.48,78.58,-0.53,0,False,False
20260821,81.4,0.48,79.63,0.6,79.12,0.54,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1102 | 亞泥 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | stale_signal | 1.事實發生日:自民國115/6/24至民國115/6/24 2.本次新增（減少）投資方式: 亞東工業投資私人有限公司100%直接持有之亞東投資有限公司以發行新股 方式取得亞東工業投資私人有限公司持有之江西亞東水泥有限公司85%股權， 股份交換後本公司間接投資大陸金額增加。 3.董事會通過日期: 民國115年6月24日 4.其他核決日期: 不適用 5.交易單位數量、每單位價格及交易總金額: 交易總金額人民幣5,437,557,443.53元 6.大陸被投資公司之公司名稱: 江西亞東水泥有限公司 7.前開大陸被投資公司之實收資本額: 美金356,104仟元 8.前開大陸被投資公司本次擬新增資本額: 不適用 9.前開大陸被投資公司主要營業項目: 熟料、水泥的生產及銷售 10.前開大陸被投資公司最近年度財務報表會計師意見型態: 無保留意見 11.前開大陸被投資公司最近年度財務報表權益總額: 人民幣6,460,726仟元 12.前開大陸被投資公司最近年度財務報表損益金額: 人民幣123,516仟元 13.迄目前為止，對前開大陸被投資公司之實際投資金額: 美金277,505仟元 14.交易相對人及其與公司之關係: 1.亞東工業投資私人有限公司直接持有亞東投資有限公司100%股權及江西亞東水泥 有限公司85%股權； 2.亞東投資有限公司為亞東工業投資私人有限公司100%直接持有之子公司， 並直接持有江西亞東水泥有限公司10%股權； 3.亞東工業投資私人有限公司及亞東投資有限公司皆為本公司間接持有之重要子公司。 15.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉 之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期及移轉金額: 1.選定關係人為交易對象之原因：集團內部組織架構調整； 2.前次移轉之所有人：亞洲投資私人有限公司； 3.前次移轉之所有人與公司之關係：亞洲投資私人有限公司為本公司 間接持有之重要子公司； 4.前次移轉之所有人與交易相對人之關係：亞洲投資私人有限公司100% 直接持有亞東工業投資私人有限公司； 5.前次移轉日期：114年4月29日； 6.前次交易總金額：人民幣5,386,628,948.48元。 16.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取得 及處分日期、價格及交易當時與公司之關係: 1.亞東工業投資私人有限公司取得江西亞東水泥有限公司85%股權日期： 114年4月29日 2.亞東工業投資私人有限公司取得江西亞東水泥有限公司85%股權價格： 人民幣5,386,628,948.48元 3.所有權人亞東工業投資私人有限公司交易當時與公司之關係： 為本公司間接持有之重要子公司。 17.處分利益（或損失）: 不適用 18.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定事項: 交付或付款條件：以股份交換方式執行 契約限制條款及其他重要約定事項：無 19.本次交易之決定方式、價格決定之參考依據及決策單位: 本次交易之決定方式：依亞東工業投資私人有限公司與亞東投資有限公司董事會決議辦理 價格決定之參考依據：江西亞東水泥有限公司115年4月30日財務報表之帳面淨值 決策單位：亞東工業投資私人有限公司與亞東投資有限公司董事會 20.經紀人: 無 21.取得或處分之具體目的: 集團內部組織架構調整 22.本次交易表示異議董事之意見: 無 23.本次交易為關係人交易:是 24.監察人承認或審計委員會同意日期: 民國115年06月24日 25.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）: 美金4,158,892仟元 26.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 實收資本額之比率: 370.85% 27.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 總資產之比率: 52.4% 28.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 歸屬於母公司業主之權益之比率: 72.96% 29.迄目前為止，實際赴大陸地區投資總額: 美金2,184,042仟元 30.迄目前為止，實際赴大陸地區投資總額占最近期財務報表實收資本額之比率: 194.75% 31.迄目前為止，實際赴大陸地區投資總額占最近期財務報表總資產之比率: 27.52% 32.迄目前為止，實際赴大陸地區投資總額占最近期財務報表歸屬於母公司業主之權益之比率: 38.31% 33.最近三年度認列投資大陸損益金額: 112年 人民幣263,978仟元 113年 人民&#24164;-906仟元 114年 人民幣181,776仟元 34.最近三年度獲利匯回金額: 112年 人民幣169,793仟元 113年 人民幣43,510仟元 114年 人民幣0仟元 35.本次交易會計師出具非合理性意見:否 36.會計師事務所名稱: 致和聯合會計師事務所 37.會計師姓名: 施炳全 38.會計師開業證書字號: 北市會證字第3325號 39.前已就同一件事件發布重大訊息日期: 不適用 40.其他敘明事項: 本案需經投審司核准後實行；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1102 | 亞泥 | 2 | 2 | 2 | 2 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1102 | 亞泥 | 2 | 0 | 1050530.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
