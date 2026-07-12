# INDIVIDUAL STOCK CHATGPT PACKET - 3264 欣銓

## Metadata
- generated_at: 2026-07-12 22:27:02 Asia/Taipei
- stock_id: 3264
- stock_name: 欣銓
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 166
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3264_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3264_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3264_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3264_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3264_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3264_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3264_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3264_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3264_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3264_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3264_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3264_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3264.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3264.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3264.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3264.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3264_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3264_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3264_latest.md?ref=main

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
- date: 20260709
- open: 234
- high: 239
- low: 229.5
- close: 235
- volume: 4950000
- ma5: 240.5
- ema23_primary: 230.91
- distance_to_ema23_pct: 1.77
- ma20: 230.4
- ma60: 220.89
- ma120: 186.75
- return_5d: -5.62
- return_20d: 11.11
- volume_ratio: 0.56
- distance_to_ma20_pct_auxiliary: 2
- distance_to_high_60_pct: -13.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,210,217,204.5,215,5027000,219.97,-2.26,223.35,199.08,1.28
20260612,224.5,233,224,227.5,9098000,220.6,3.13,223.43,200.26,2.66
20260615,235,238,228,228,5262000,221.22,3.07,223.32,201.47,1.55
20260616,233,233.5,219.5,220,3885000,221.11,-0.5,223.6,202.57,1.29
20260617,219.5,219.5,208,211.5,9141000,220.31,-4,223.85,203.56,3.17
20260618,213,232.5,213,232.5,13921000,221.33,5.05,224.53,205.02,4.26
20260622,238,248,238,242,14378000,223.05,8.5,225.55,206.62,3.62
20260623,243,251.5,233,233.5,13695000,223.92,4.28,226.03,207.94,2.95
20260624,233,235.5,226,234.5,6408000,224.8,4.31,226.2,209.35,1.29
20260625,239.5,243.5,227.5,228,5618000,225.07,1.3,226.12,210.52,1.08
20260626,230,232,212,214.5,6988000,224.19,-4.32,225.07,211.39,1.26
20260629,214.5,223,213.5,215.5,4787000,223.46,-3.56,223.68,212.39,0.83
20260630,215.5,228,215.5,222,6689000,223.34,-0.6,223.62,213.32,1.09
20260701,227,237.5,227,232,10264000,224.06,3.54,224.5,214.51,1.55
20260702,227.5,249.5,223.5,249,9703000,226.14,10.11,225.47,216.06,1.37
20260703,241.5,251,236,247,10406000,227.88,8.39,226,217.43,1.37
20260706,268,271.5,254.5,257,18551000,230.31,11.59,227.43,218.71,2.18
20260707,259.5,262,231.5,231.5,13058000,230.41,0.47,228.45,219.42,1.46
20260708,235.5,235.5,222.5,232,5114000,230.54,0.63,229.22,220.09,0.57
20260709,234,239,229.5,235,4950000,230.91,1.77,230.4,220.89,0.56
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 71.99
- over_600_ratio: 69.39
- over_800_ratio: 66.5
- over_1000_ratio: 65.22
- over_400_change_1w: 0.98
- over_800_change_1w: 0.74
- over_1000_change_1w: 0.52
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,71.69,,66.36,,63.8,,0,False,False
20260508,72.4,0.71,67.28,0.92,64.53,0.73,1,True,True
20260515,70.94,-1.46,66.21,-1.07,63.48,-1.05,0,False,False
20260522,70.76,-0.18,66.13,-0.08,63.97,0.49,1,False,True
20260529,72.25,1.49,67.02,0.89,64.3,0.33,2,True,True
20260605,70.55,-1.7,65.07,-1.95,62.94,-1.36,0,False,False
20260612,69.52,-1.03,63.7,-1.37,61.47,-1.47,0,False,False
20260618,68.97,-0.55,63.13,-0.57,61.26,-0.21,0,False,False
20260626,71.01,2.04,65.76,2.63,64.7,3.44,1,True,True
20260703,71.99,0.98,66.5,0.74,65.22,0.52,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3264 | 欣銓 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 廠務工程 2.事實發生日:115/3/10~115/6/18 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:依本公司核決權限規定辦理 民國115年6月18日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 交易數量：一批；本批交易總金額：NTD 738,801,000 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人 : 和碩工程股份有限公司 與公司之關係：無。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用。 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 採電匯或信用狀付款。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易決定方式: 比價及議價 價格決定: 依市場行情 決策單位: 依本公司核決權限規定辦理 12.專業估價者事務所或公司名稱及其估價金額: 不適用。 13.專業估價師姓名: 不適用。 14.專業估價師開業證書字號: 不適用。 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用。 19.會計師事務所名稱: 不適用。 20.會計師姓名: 不適用。 21.會計師開業證書字號: 不適用。 22.經紀人及經紀費用: 不適用。 23.取得或處分之具體目的或用途: 配合營運需求。 24.本次交易表示異議之董事之意見: 不適用。 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用。 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |
| 20260709 | 3264 | 欣銓 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 廠務工程 2.事實發生日:115/3/10~115/6/18 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:依本公司核決權限規定辦理 民國115年6月18日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 交易數量：一批；本批交易總金額：NTD 738,801,000 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人 : 和碩工程股份有限公司 與公司之關係：無。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用。 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 採電匯或信用狀付款。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易決定方式: 比價及議價 價格決定: 依市場行情 決策單位: 依本公司核決權限規定辦理 12.專業估價者事務所或公司名稱及其估價金額: 不適用。 13.專業估價師姓名: 不適用。 14.專業估價師開業證書字號: 不適用。 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用。 19.會計師事務所名稱: 不適用。 20.會計師姓名: 不適用。 21.會計師開業證書字號: 不適用。 22.經紀人及經紀費用: 不適用。 23.取得或處分之具體目的或用途: 配合營運需求。 24.本次交易表示異議之董事之意見: 不適用。 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用。 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3264 | 欣銓 | 14 | 3 | 5 | 10 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
