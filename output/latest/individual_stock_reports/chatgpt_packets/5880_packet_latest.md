# INDIVIDUAL STOCK CHATGPT PACKET - 5880 合庫金

## Metadata
- generated_at: 2026-06-25 22:24:09 Asia/Taipei
- stock_id: 5880
- stock_name: 合庫金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260624
- price_rows: 290
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5880_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5880_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5880.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5880.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5880.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5880.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5880_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5880_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5880_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260624
- open: 24.5
- high: 24.65
- low: 24.3
- close: 24.4
- volume: 18131110
- ma5: 24.58
- ema23_primary: 23.85
- distance_to_ema23_pct: 2.29
- ma20: 23.75
- ma60: 23.4
- ma120: 23.59
- return_5d: -0.81
- return_20d: 7.49
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: 2.74
- distance_to_high_60_pct: -2.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260527,22.7,22.8,22.65,22.75,16022020,22.9,-0.66,22.84,23.22,0.96
20260528,22.75,22.8,22.6,22.7,21036566,22.89,-0.81,22.82,23.2,1.25
20260529,22.7,22.85,22.6,22.85,71316116,22.88,-0.14,22.82,23.18,3.64
20260601,22.85,22.95,22.6,22.85,29130456,22.88,-0.13,22.81,23.17,1.44
20260602,22.8,23.1,22.7,23.05,31996097,22.89,0.68,22.82,23.16,1.51
20260603,23.1,23.5,22.95,23.4,31552327,22.94,2.02,22.84,23.16,1.43
20260604,23.4,24,23.35,23.7,44263958,23,3.04,22.88,23.18,1.91
20260605,23.7,23.7,23.3,23.45,28747769,23.04,1.79,22.9,23.18,1.21
20260608,23,23.35,22.9,23.05,28384272,23.04,0.05,22.9,23.18,1.16
20260609,23.05,24,23.05,23.85,46115818,23.11,3.22,22.95,23.19,1.8
20260610,23.6,23.95,23.6,23.8,24784314,23.16,2.75,23,23.2,0.95
20260611,23.9,23.9,23.6,23.85,23269984,23.22,2.71,23.05,23.22,0.88
20260612,24.25,24.25,23.9,24.05,26503384,23.29,3.26,23.11,23.23,0.99
20260615,24.3,24.35,24,24.15,21471650,23.36,3.37,23.19,23.25,0.79
20260616,24.25,24.7,24.1,24.6,41356167,23.46,4.84,23.28,23.27,1.47
20260617,24.55,25,24.5,24.75,28807379,23.57,5,23.38,23.3,1
20260618,24.75,25,24.7,24.75,33174894,23.67,4.56,23.48,23.34,1.11
20260622,24.75,24.75,24.35,24.45,23219136,23.74,3.01,23.57,23.37,0.77
20260623,24.35,24.65,24.3,24.55,23831499,23.8,3.14,23.66,23.39,0.78
20260624,24.5,24.65,24.3,24.4,18131110,23.85,2.29,23.75,23.4,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 73.3
- over_600_ratio: 71.23
- over_800_ratio: 70.1
- over_1000_ratio: 69.28
- over_400_change_1w: 0.3
- over_800_change_1w: 0.33
- over_1000_change_1w: 0.31
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.94,,69.68,,68.88,,0,False,False
20260508,72.89,-0.05,69.63,-0.05,68.83,-0.05,0,False,False
20260515,72.73,-0.16,69.44,-0.19,68.6,-0.23,0,False,False
20260522,72.59,-0.14,69.32,-0.12,68.48,-0.12,0,False,False
20260529,72.51,-0.08,69.22,-0.1,68.4,-0.08,0,False,False
20260605,72.76,0.25,69.51,0.29,68.68,0.28,1,True,True
20260612,73,0.24,69.77,0.26,68.97,0.29,2,True,True
20260618,73.3,0.3,70.1,0.33,69.28,0.31,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 5880 | 合庫金 | pattern | 型態觀察 | 54.0 |  |  | base_building |  |  | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 合作金庫金融控股股份有限公司無擔保主順位普通公司債 2.事實發生日:115/6/24~115/6/24 3.董事會通過日期: 民國115年6月24日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量：視市場狀況決定之 單位價格：依票面金額十足發行 交易總金額：上限新臺幣100億元整 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人：合作金庫金融控股股份有限公司 與公司之關係：利害關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 選定關係人為交易對象之原因： 擔任合作金庫金融控股股份有限公司無擔保主順位普通公司債之主辦承銷商 前次移轉之所有人:不適用 前次移轉日期:不適用 前次移轉金額:不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 交割日一次付清 12.本次交易之決定方式、價格決定之參考依據及決策單位: 交易之決定方式：議價 價格決定之參考依據：依議價結果 決策單位：董事會 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 不適用 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: （1）占總資產之比例：71.60% （2）占歸屬於母公司業主之權益之比例：358.28% （3）最近期財務報表中營運資金數額：6,029,650,577元 16.經紀人及經紀費用: 不適用 17.取得或處分之具體目的或用途: 因擔任合作金庫金融控股股份有限公司無擔保主順位普通公司債 之主辦承銷商而協助發行事宜 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:是 20.監察人承認或審計委員會同意日期: 民國115年6月24日 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 卓群聯合會計師事務所 23.會計師姓名: 陳詠捷會計師 24.會計師開業證書字號: 金管會證字第7809號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用 28.資金來源: 營運資金 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 5880 | 合庫金 | 20 | 10 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
