# INDIVIDUAL STOCK CHATGPT PACKET - 5347 世界

## Metadata
- generated_at: 2026-07-27 22:27:30 Asia/Taipei
- stock_id: 5347
- stock_name: 世界
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 171
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5347_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5347_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5347_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5347_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5347_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5347_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5347_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5347_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5347_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5347_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5347_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5347_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5347.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5347.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5347.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5347.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5347_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5347_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5347_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260717
- open: 170
- high: 173
- low: 169
- close: 169
- volume: 30657000
- ma5: 179.1
- ema23_primary: 182.11
- distance_to_ema23_pct: -7.2
- ma20: 190
- ma60: 171.22
- ma120: 149.24
- return_5d: -2.31
- return_20d: 1.5
- volume_ratio: 0.88
- distance_to_ma20_pct_auxiliary: -11.05
- distance_to_high_60_pct: -24.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,167,174.5,165,174.5,16874000,164.88,5.83,166.1,150.25,1.48
20260622,191.5,191.5,191.5,191.5,15116000,167.1,14.6,167.57,151.56,1.25
20260623,201.5,201.5,183.5,186.5,63729000,168.72,10.54,168.47,152.6,4.16
20260624,190,200,183.5,200,67059000,171.32,16.74,170.22,153.98,3.59
20260625,202,220,195,220,73115000,175.38,25.44,172.93,155.64,3.28
20260626,215,215.5,200,202,60513000,177.6,13.74,174.95,157.06,2.39
20260629,206.5,215.5,203.5,208.5,37217000,180.17,15.72,176.97,158.6,1.37
20260630,216.5,223,213,216,36918000,183.16,17.93,178.82,160.23,1.27
20260701,219.5,223,202.5,204.5,30364000,184.94,10.58,180.47,161.81,0.99
20260702,199.5,201.5,192.5,198,25432000,186.03,6.44,181.97,163.09,0.8
20260703,195.5,195.5,192,193.5,17207000,186.65,3.67,183.5,164.13,0.53
20260706,193,193.5,182.5,185,27184000,186.51,-0.81,184.68,165.03,0.8
20260707,186,186.5,173,175,27650000,185.55,-5.69,185.6,165.79,0.82
20260708,176,176.5,168,176.5,25030000,184.8,-4.49,186.38,166.64,0.74
20260709,177.5,178,170.5,173,20279000,183.82,-5.88,187.4,167.45,0.6
20260713,181.5,187,176,178.5,28422000,183.37,-2.66,188.25,168.3,0.85
20260714,178.5,182,163.5,174,20625000,182.59,-4.71,188.47,168.99,0.63
20260715,178,189.5,174.5,186.5,35879000,182.92,1.96,189.07,169.9,1.09
20260716,185,192,183,187.5,41008000,183.3,2.29,189.88,170.71,1.2
20260717,170,173,169,169,30657000,182.11,-7.2,190,171.22,0.88
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 85.13
- over_600_ratio: 83.66
- over_800_ratio: 82.44
- over_1000_ratio: 81.61
- over_400_change_1w: -0.4
- over_800_change_1w: -0.55
- over_1000_change_1w: -0.33
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,85.34,,82.76,,81.9,,0,False,False
20260508,87.54,2.2,84.84,2.08,83.93,2.03,1,True,True
20260515,86.39,-1.15,83.93,-0.91,82.88,-1.05,0,False,False
20260522,85.77,-0.62,83.3,-0.63,82.45,-0.43,0,False,False
20260529,85.49,-0.28,82.87,-0.43,81.92,-0.53,0,False,False
20260605,85.26,-0.23,82.7,-0.17,81.76,-0.16,0,False,False
20260612,85.09,-0.17,82.78,0.08,81.54,-0.22,1,False,True
20260618,85.82,0.73,83.62,0.84,82.47,0.93,2,True,True
20260626,87.35,1.53,84.87,1.25,83.7,1.23,3,True,True
20260703,86.46,-0.89,83.96,-0.91,82.85,-0.85,0,False,False
20260709,85.53,-0.93,82.99,-0.97,81.94,-0.91,0,False,False
20260717,85.13,-0.4,82.44,-0.55,81.61,-0.33,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 5347 | 世界 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  |  | repeated_but_no_breakout | 1.證券名稱: Sumitomo Mitsui Financial Group, Inc.之普通公司債 2.交易日期:115/2/2~115/7/9 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:副總經理暨財務長 民國115年01月27日 5.交易數量、每單位價格及交易總金額: (1)US86562MEJ53：40,000單位；每單位約US$99.202元；總金額US$4佰萬元。 (2)US86562MDM91：80,000單位；每單位約US$102.79元；總金額US$8佰萬元。 (3)US86562MBP41：60,000單位；每單位約US$96.26元；總金額US$6佰萬元。 6.處分利益（或損失）（取得有價證券者不適用）: 不適用 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: (1)數量:180,000單位  (2)金額:US$18佰萬元  (3)持股比例：不適用  (4)權利受限情形: 無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: (1)有價證券投資(含本次交易)占公司最近期財務報表中總資產之比例：5.90% (2)占公司最近期財務報表歸屬於母公司業主之權益之比例：10.66% (3)最近期財報中營運資金（總資產減總負債）數額:20,206,163仟元 10.取得或處分之具體目的: 固定收益投資 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 無 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 5347 | 世界 | 9 | 2 | 5 | 9 | 15 | repeated_but_no_breakout | 近 10 日上榜 9 次、近 20 日上榜 15 次，但尚未有效突破，需等待攻擊確認。 |

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
