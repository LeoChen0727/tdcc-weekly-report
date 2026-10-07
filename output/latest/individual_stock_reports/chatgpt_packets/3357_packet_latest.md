# INDIVIDUAL STOCK CHATGPT PACKET - 3357 臺慶科

## Metadata
- generated_at: 2026-10-07 22:17:59 Asia/Taipei
- stock_id: 3357
- stock_name: 臺慶科
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 266
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3357_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3357_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3357_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3357_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3357_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3357_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3357_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3357_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3357_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3357_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3357_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3357_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3357.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3357.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3357.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3357.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3357_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3357_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3357_latest.md?ref=main

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
- model_category_display_zh: 營收爆發低反應股
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收爆發低反應股 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收爆發低反應股 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20261002
- open: 213
- high: 219
- low: 211.5
- close: 215.5
- volume: 1817000
- ma5: 208.3
- ema23_primary: 208.81
- distance_to_ema23_pct: 3.2
- ma20: 206.32
- ma60: 214.68
- ma120: 230.18
- return_5d: 4.61
- return_20d: 3.11
- volume_ratio: 1.71
- distance_to_ma20_pct_auxiliary: 4.45
- distance_to_high_60_pct: -23.45

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,210.5,211,203,203,927000,216.47,-6.22,217.22,246.16,0.46
20260904,206.5,215.5,206.5,214,1613000,216.27,-1.05,217.57,244.8,0.81
20260907,221,221,213.5,213.5,1957000,216.04,-1.17,217.35,243.57,0.98
20260908,210.5,213,206,206.5,989000,215.24,-4.06,216.72,242.13,0.53
20260909,207,210.5,207,208,492000,214.64,-3.09,215.6,240.23,0.29
20260910,209,210.5,202.5,207,883000,214,-3.27,213.28,238.67,0.57
20260911,203,210,201,201,839000,212.92,-5.6,211.9,236.74,0.62
20260914,197,202,194.5,199,669000,211.76,-6.02,210.85,234.26,0.52
20260915,200,204.5,199,199,559000,210.7,-5.55,210.15,231.8,0.45
20260916,202,202,198,201,435000,209.89,-4.23,209.28,229.9,0.38
20260917,203,205,199,200,510000,209.06,-4.34,208.57,227.91,0.46
20260918,203,207.5,201.5,207.5,2751000,208.93,-0.69,208.43,226.1,2.26
20260921,207.5,210.5,204,209,1018000,208.94,0.03,208.38,224.57,0.82
20260922,213,217.5,206,210.5,1418000,209.07,0.68,208.43,223.25,1.12
20260923,209.5,214.5,206,206,713000,208.81,-1.35,208.25,221.37,0.57
20260924,205.5,208,203,206,792000,208.58,-1.24,207.7,219.71,0.64
20260929,204,206,202.5,203,419000,208.11,-2.46,206.7,218.11,0.39
20260930,204.5,207,204,204.5,357000,207.81,-1.59,206.15,216.65,0.36
20261001,206,217,206,212.5,2066000,208.2,2.06,206,215.46,2.02
20261002,213,219,211.5,215.5,1817000,208.81,3.2,206.32,214.68,1.71
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 57.1
- over_600_ratio: 52.54
- over_800_ratio: 44.51
- over_1000_ratio: 41.44
- over_400_change_1w: -0.26
- over_800_change_1w: 0.04
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,57.99,-0.09,44.88,0.95,42.52,0.87,2,False,True
20260724,58.21,0.22,45.41,0.53,42.41,-0.11,3,False,True
20260731,58.22,0.01,44.81,-0.6,42.56,0.15,4,False,True
20260807,58.61,0.39,44.28,-0.53,42.72,0.16,5,False,True
20260814,58.38,-0.23,45.5,1.22,42.46,-0.26,6,False,True
20260821,57.48,-0.9,43.6,-1.9,42.04,-0.42,0,False,False
20260828,57.4,-0.08,43.6,0,42.04,0,0,False,False
20260904,56.67,-0.73,42.73,-0.87,41.17,-0.87,0,False,False
20260911,57.25,0.58,42.71,-0.02,41.15,-0.02,1,False,False
20260918,57.49,0.24,43.86,1.15,41.62,0.47,2,True,True
20260924,57.36,-0.13,44.47,0.61,41.44,-0.18,3,False,True
20261002,57.1,-0.26,44.51,0.04,41.44,0,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 3357 | 臺慶科 | revenue_breakout_low_response | 營收爆發低反應股 | 17 | 7 | A_優先追蹤 |  |  |  | continued_2_3d | 1.證券名稱: 萬潤科技股份有限公司普通股 2.交易日期:115/6/24~116/6/23 3.董事會通過日期: 民國115年6月24日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量:含115年4月處分180,000股,總數量不超過500,000股 每單位價格：以實際交易日市價及金額辦理 交易總金額：依股票實際成交價格及交割股數為準，處分金額依法另行公告 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分為出售透過其他綜合損益按公允價值衡量之金融資產， 處分結果將計入資產負債表之權益項下，並不影響本公司當期損益 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 435,000股；帳面價值NT$487,200仟元；0.45%；無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 76.38%；114.05%；NT$-362,230仟元。 10.取得或處分之具體目的: 活化資產，充實營運資金。 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 民國115年6月24日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 114年度個體財報,流動負債中含可轉換公司債917,618仟元,導致營運資金為負數。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20261002 | 3357 | 臺慶科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_2_3d | 1.證券名稱: 萬潤科技股份有限公司普通股 2.交易日期:115/6/24~116/6/23 3.董事會通過日期: 民國115年6月24日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量:含115年4月處分180,000股,總數量不超過500,000股 每單位價格：以實際交易日市價及金額辦理 交易總金額：依股票實際成交價格及交割股數為準，處分金額依法另行公告 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分為出售透過其他綜合損益按公允價值衡量之金融資產， 處分結果將計入資產負債表之權益項下，並不影響本公司當期損益 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 435,000股；帳面價值NT$487,200仟元；0.45%；無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 76.38%；114.05%；NT$-362,230仟元。 10.取得或處分之具體目的: 活化資產，充實營運資金。 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 民國115年6月24日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 114年度個體財報,流動負債中含可轉換公司債917,618仟元,導致營運資金為負數。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 3357 | 臺慶科 | 2 | 2 | 2 | 5 | 9 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
