# INDIVIDUAL STOCK CHATGPT PACKET - 8936 國統

## Metadata
- generated_at: 2026-08-08 22:29:09 Asia/Taipei
- stock_id: 8936
- stock_name: 國統
- packet_status: standard_180d_window_packet
- latest_price_date: 20260805
- price_rows: 184
- current_main_price_date: 20260805
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260807-01698d0b1c2355ac
- official_tdcc_signal_date: 20260807
- latest_tdcc_date: 20260807
- tdcc_rows: 15
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8936_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8936_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8936_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8936_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8936_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8936_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8936_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8936_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8936_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8936_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8936_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8936_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8936.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8936.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8936.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8936.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8936_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8936_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8936_latest.md?ref=main

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
- date: 20260805
- open: 52.1
- high: 52.3
- low: 51.7
- close: 52.1
- volume: 1133000
- ma5: 51.4
- ema23_primary: 53.15
- distance_to_ema23_pct: -1.98
- ma20: 52.84
- ma60: 54.34
- ma120: 53.01
- return_5d: 2.56
- return_20d: -6.8
- volume_ratio: 0.88
- distance_to_ma20_pct_auxiliary: -1.4
- distance_to_high_60_pct: -20.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,56.2,56.3,55,56.1,1625000,57.3,-2.1,57.88,53.74,0.19
20260709,56.3,56.4,55.6,55.6,1212000,57.16,-2.73,57.92,53.83,0.15
20260713,56.2,56.3,55,55.1,1414000,56.99,-3.31,57.91,53.91,0.18
20260714,55.1,55.1,53.2,53.9,2286000,56.73,-4.99,57.81,53.97,0.31
20260715,54.2,55.1,54.2,54.9,1064000,56.58,-2.97,57.66,54.05,0.16
20260716,55.2,55.6,54.8,54.8,1231000,56.43,-2.89,57.6,54.13,0.19
20260717,54.3,54.7,52,52,3216000,56.06,-7.24,57.45,54.15,0.49
20260720,52.5,52.7,50.9,51.9,1298000,55.71,-6.85,57.14,54.17,0.21
20260721,52.6,52.9,52.1,52.5,708000,55.45,-5.31,56.74,54.2,0.14
20260722,52.5,53.2,52.5,52.7,907000,55.22,-4.56,56.47,54.25,0.19
20260723,53.2,53.3,52.3,52.4,758000,54.98,-4.7,56.2,54.3,0.16
20260724,52.4,52.9,52.2,52.5,766000,54.78,-4.15,55.85,54.35,0.17
20260727,53.4,53.4,52.1,53.1,731000,54.64,-2.81,55.57,54.39,0.18
20260728,52.5,52.5,51,51.5,1806000,54.37,-5.29,55.15,54.41,0.5
20260729,52.1,52.1,50,50.8,2098000,54.08,-6.06,54.44,54.39,0.76
20260730,50.5,51.1,50.2,50.2,1017000,53.75,-6.61,53.95,54.36,0.54
20260731,51.5,51.9,51.3,51.8,1062000,53.59,-3.34,53.62,54.34,0.61
20260803,51.8,52.2,51.3,51.4,873000,53.41,-3.76,53.31,54.32,0.57
20260804,51.4,51.7,51.1,51.5,668000,53.25,-3.29,53.03,54.31,0.48
20260805,52.1,52.3,51.7,52.1,1133000,53.15,-1.98,52.84,54.34,0.88
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 31.69
- over_600_ratio: 28.85
- over_800_ratio: 26.4
- over_1000_ratio: 23.24
- over_400_change_1w: 0.52
- over_800_change_1w: 0.09
- over_1000_change_1w: -0.29
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,32.45,-0.48,26.94,-0.51,24.39,-0.16,0,False,False
20260529,33.6,1.15,28.29,1.35,25.35,0.96,1,True,True
20260605,35.3,1.7,29.33,1.04,26.83,1.48,2,True,True
20260612,33.47,-1.83,26.96,-2.37,23.78,-3.05,0,False,False
20260618,33.26,-0.21,27.33,0.37,24.2,0.42,1,False,True
20260626,33,-0.26,27.46,0.13,23.56,-0.64,2,False,True
20260703,33.5,0.5,26.9,-0.56,24.88,1.32,3,False,True
20260709,32.37,-1.13,26.56,-0.34,23.4,-1.48,0,False,False
20260717,32.53,0.16,26.26,-0.3,23.48,0.08,1,False,True
20260724,31.68,-0.85,26.03,-0.23,22.93,-0.55,0,False,False
20260731,31.17,-0.51,26.31,0.28,23.53,0.6,1,False,True
20260807,31.69,0.52,26.4,0.09,23.24,-0.29,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8936 | 國統 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  |  | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 本公司之&#12070;公司國洋環境科技股份有限公司擬與苗栗縣政府 簽訂&#65378;促進&#11936;間參與苗栗縣&#12149;南頭份(包括&#12220;速公路頭份交流 道)污&#12116;下&#12116;道系統建設之興建營運移轉計畫&#65379;第四期增修協議書 2.事實發生日:115/6/30~115/6/30 3.董事會通過日期: 民國115年6月30日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 合約金額為新台幣14.42077億元(未稅) 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 苗栗縣政府，與公司關係：無。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依合約約定按期計價付款。 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依98年3月24日與苗栗縣政府簽訂合約作業。 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 不適用。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 不適用。 16.經紀人及經紀費用: 不適用。 17.取得或處分之具體目的或用途: 依據苗栗縣政府&#65378;促進&#11936;間參與苗栗縣&#12149;南頭份(包括&#12220;速 公路頭份交流道)污&#12116;下&#12116;道系統建設之興建營運移轉計畫&#65379; 第四期增修協議書興建及營運。 18.本次交易表示異議董事之意見: 無。 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用。 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用。 23.會計師姓名: 不適用。 24.會計師開業證書字號: 不適用。 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用。 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用。 28.資金來源: 不適用。 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: (1)本案經國洋公司6/30董事會決議通過，後續將與苗栗縣 政府簽訂&#65378;促進&#11936;間參與苗栗縣&#12149;南頭份(包括&#12220;速公路頭份 交流道)污&#12116;下&#12116;道系統建設之興建營運移轉計畫&#65379;第四期增 修協議書。該工程投入成本，根據國際會計準則IFRIC 12  服務特許權協議之規定，完工後帳列無形資產項下。 (2)國洋公司與苗栗縣政府簽訂第四期增修協議書後，擬委由 本公司承攬第四期計畫管網及用戶接管工程合約。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8936 | 國統 | 2 | 2 | 4 | 7 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
