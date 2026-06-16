# INDIVIDUAL STOCK CHATGPT PACKET - 2891 中信金

## Metadata
- generated_at: 2026-06-16 22:23:04 Asia/Taipei
- stock_id: 2891
- stock_name: 中信金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260616
- price_rows: 282
- latest_tdcc_date: 20260612
- tdcc_rows: 7
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2891_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2891_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2891_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2891_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2891_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2891_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2891_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2891_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2891_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2891_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2891_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2891_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2891.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2891.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2891.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2891.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2891_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2891_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2891_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- risk_control_zh: TDCC 歷史不足
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足

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
- insufficient_tdcc_history

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260616
- open: 70.4
- high: 71.7
- low: 69.6
- close: 70.8
- volume: 40981294
- ma5: 68.52
- ema23_primary: 62.43
- distance_to_ema23_pct: 13.4
- ma20: 61.76
- ma60: 56.24
- ma120: 53.38
- return_5d: 10.45
- return_20d: 29.2
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: 14.64
- distance_to_high_60_pct: -2.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260515,55.1,55.6,54.7,54.8,36032190,54.04,1.4,53.84,53.12,0.7
20260518,55,55.4,54.4,54.8,30347395,54.1,1.29,53.92,53.17,0.59
20260519,55.3,56.6,54.9,55.4,60742665,54.21,2.19,54.03,53.23,1.17
20260520,56.4,58,55.6,57.8,114703217,54.51,6.03,54.27,53.33,2.08
20260521,57.9,58.6,57.2,57.5,72093148,54.76,5,54.48,53.42,1.27
20260522,57.5,58.2,57.2,57.6,37279590,55,4.73,54.72,53.48,0.66
20260525,58.2,58.2,57,57.3,46056452,55.19,3.83,54.94,53.54,0.82
20260526,57.3,58.7,57.3,57.6,51792760,55.39,3.99,55.19,53.61,0.91
20260527,58.5,60.2,57.6,59.2,65196446,55.71,6.27,55.48,53.66,1.13
20260528,58.6,60.8,58.6,59.3,69083306,56.01,5.88,55.79,53.76,1.18
20260529,59.4,61.4,59.4,60.5,113545993,56.38,7.31,56.2,53.87,1.84
20260601,60.5,62.6,60.5,62.1,43910039,56.86,9.22,56.66,54.06,0.71
20260602,62,64.4,61.8,64.1,70381891,57.46,11.55,57.19,54.27,1.13
20260603,65.4,70.5,64.3,70.5,84076949,58.55,20.41,57.98,54.59,1.33
20260604,62,64.4,61.8,64.1,70381891,59.01,8.62,58.38,54.81,1.12
20260605,66.3,68,66,66.6,63844979,59.64,11.66,58.88,55.07,1.01
20260611,68.5,68.5,66.5,67.5,63717773,60.3,11.94,59.49,55.34,1
20260612,67.8,69.2,66.9,67.6,83389953,60.91,10.99,60.2,55.61,1.31
20260615,71.7,72.6,69,70.1,42928285,61.67,13.67,60.96,55.92,0.68
20260616,70.4,71.7,69.6,70.8,40981294,62.43,13.4,61.76,56.24,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 82.11
- over_600_ratio: 80.98
- over_800_ratio: 80.11
- over_1000_ratio: 79.37
- over_400_change_1w: 0
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,81.47,,79.35,,78.6,,0,False,False
20260508,81.68,0.21,79.58,0.23,78.84,0.24,1,True,True
20260515,81.67,-0.01,79.6,0.02,78.84,0,2,False,True
20260522,81.95,0.28,79.91,0.31,79.19,0.35,3,True,True
20260529,81.98,0.03,79.95,0.04,79.24,0.05,4,True,True
20260605,82.11,0.13,80.12,0.17,79.41,0.17,5,True,True
20260612,82.11,0,80.11,-0.01,79.37,-0.04,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260616 | 2891 | 中信金 | pattern | 型態觀察 | 46.0 |  |  | base_building |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 金融機構債權(放款) 2.事實發生日:115/6/15~115/6/15 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:信審會 民國115年03月13日 5.交易單位數量、每單位價格及交易總金額: 不適用 不適用 USD 14,290,000 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 1.KfW IPEX-Bank GmbH 2.Hua Nan Commercial Bank, Ltd., Offshore Banking Branch 3.Arab Bank for Investment and Foreign Trade 4.Bank of China (Hong Kong) Limited 5.Bank of China (Malaysia) Berhad 6.BDO Unibank, Inc. (Singapore Branch) 7.China Construction Bank Corporation, Labuan Branch 8.Doha Bank Q.P.S.C. 9.Far Eastern International Bank, Ltd. 10.Land Bank of Taiwan, Singapore Branch 11.Mega International Commercial Bank Co., Ltd., Offshore Banking Branch 12.Taiwan Cooperative Bank, Offshore Banking Branch 13.Union Bank of Taiwan Co., Ltd. 14.First Commercial Bank, Offshore Banking Branch 15.Taiwan Shin Kong Commercial Bank Co., Ltd 16.Chang Hwa Commercial Bank, Ltd. Offshore Banking Branch 17.E.SUN Commercial Bank, Ltd. 18.Sunny Bank, Ltd. 19.Taichung Commercial Bank Co., Limited Labuan Branch 20.The Export-Import Bank of the Republic of China 非關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表說明 認列情形）: 無。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 付款條件: 依合約辦理。 重要約定事項: 依合約辦理。 12.本次交易之決定方式、價格決定之參考依據及決策單位: 為本行內部最終審核單位核定，相關條件依合約及一般市場慣例為之。 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 不適用 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 不適用 16.經紀人及經紀費用: 不適用 17.取得或處分之具體目的或用途: 活絡債權資產組合。 18.本次交易表示異議董事之意見: 不適用 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用 23.會計師姓名: 不適用 24.會計師開業證書字號: 不適用 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 例行性業務 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 本交易係依115/06/14之匯率計算(USD 1=NTD 31.6480)。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260616 | 2891 | 中信金 | 1 | 1 | 3 | 7 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260616 | 2891 | 中信金 | 26 | 0 | 3587260.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
