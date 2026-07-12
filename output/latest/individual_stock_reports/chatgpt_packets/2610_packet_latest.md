# INDIVIDUAL STOCK CHATGPT PACKET - 2610 華航

## Metadata
- generated_at: 2026-07-12 22:26:47 Asia/Taipei
- stock_id: 2610
- stock_name: 華航
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 32
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2610_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2610_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2610_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2610_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2610_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2610_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2610_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2610_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2610_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2610_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2610_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2610_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2610.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2610.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2610.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2610.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2610_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2610_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2610_latest.md?ref=main

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
- date: 20260709
- open: 22
- high: 22
- low: 21.2
- close: 21.4
- volume: 50121544
- ma5: 22.09
- ema23_primary: 21.76
- distance_to_ema23_pct: -1.67
- ma20: 22.18
- ma60: 19.81
- ma120: 20.02
- return_5d: -6.35
- return_20d: 9.46
- volume_ratio: 0.66
- distance_to_ma20_pct_auxiliary: -3.54
- distance_to_high_60_pct: -13.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,19.55,19.65,19.25,19.45,39002241,19.11,1.8,19.04,18.59,0.7
20260612,19.85,20.7,19.8,20.4,79303652,19.21,6.17,19.13,18.62,1.35
20260615,21.35,21.7,20.95,21.4,85921129,19.4,10.33,19.29,18.66,1.39
20260616,21.5,21.5,20.95,21.2,58891339,19.55,8.46,19.43,18.7,0.92
20260617,21.3,22.35,21.1,21.85,152758333,19.74,10.7,19.61,18.75,2.16
20260618,22.1,22.4,21.8,22,100065829,19.93,10.4,19.77,18.81,1.35
20260622,21.95,22,21.25,21.8,56950265,20.08,8.55,19.93,18.86,0.75
20260623,21.95,22.6,21.75,22.3,75213791,20.27,10.03,20.11,18.91,0.97
20260624,22.6,23.6,22.25,23.25,146260216,20.52,13.32,20.34,18.99,1.76
20260625,23.8,24.75,23.7,24.2,140540321,20.82,16.22,20.62,19.08,1.61
20260626,24.2,24.25,23.1,23.2,74193002,21.02,10.36,20.86,19.16,0.84
20260629,23.7,23.9,22.95,23.1,56663975,21.19,8.99,21.05,19.25,0.75
20260630,23.55,23.7,22.9,23.7,78231000,21.4,10.73,21.26,19.34,1.04
20260701,23.7,23.7,22.3,22.55,99673000,21.5,4.89,21.41,19.41,1.28
20260702,22.65,22.95,22.3,22.85,59604000,21.61,5.73,21.56,19.49,0.76
20260703,22.6,22.95,22.45,22.55,40689054,21.69,3.97,21.69,19.55,0.52
20260706,22.6,22.75,22.35,22.45,29192000,21.75,3.2,21.82,19.62,0.38
20260707,22.45,22.55,21.8,22,53833884,21.77,1.04,21.96,19.69,0.7
20260708,22.1,22.95,21.9,22.05,53283716,21.8,1.16,22.09,19.75,0.7
20260709,22,22,21.2,21.4,50121544,21.76,-1.67,22.18,19.81,0.66
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 72.49
- over_600_ratio: 71.26
- over_800_ratio: 70.53
- over_1000_ratio: 69.73
- over_400_change_1w: 0.18
- over_800_change_1w: 0.2
- over_1000_change_1w: 0.16
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260417,68.23,-0.58,65.65,-0.51,64.73,-0.64,0,False,False
20260424,67.64,-0.59,65.08,-0.57,64.1,-0.63,0,False,False
20260430,67.43,-0.21,64.88,-0.2,63.92,-0.18,0,False,False
20260508,67.45,0.02,64.9,0.02,63.83,-0.09,1,False,True
20260515,67.77,0.32,65.26,0.36,64.27,0.44,2,True,True
20260522,67.85,0.08,65.43,0.17,64.44,0.17,3,True,True
20260529,67.62,-0.23,65.21,-0.22,64.07,-0.37,0,False,False
20260605,68.08,0.46,65.68,0.47,64.75,0.68,1,True,True
20260612,68.39,0.31,65.96,0.28,65.07,0.32,2,True,True
20260618,69.76,1.37,67.45,1.49,66.53,1.46,3,True,True
20260626,72.31,2.55,70.33,2.88,69.57,3.04,4,True,True
20260703,72.49,0.18,70.53,0.2,69.73,0.16,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2610 | 華航 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 坐落於633 Third Ave., Unit 8A, New York, NY 10017, USA之房舍 2.事實發生日:115/6/30~115/6/30 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:依『公開發行公司取得或處分資產處理準則』第15條第2項規定， 事後提報最近期董事會追認。 民國115年6月30日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 5,753平方英尺，交易總金額美金1,274,748元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：中美企業公司 與公司之關係：關係人(本公司之子公司) 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 選定關係人為交易對象之原因：地點符合營運需求 前次移轉情形：不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 每月初支付租金，115年度每月租金美金20,009元； 116年度每月租金美金20,609元； 117年度每月租金美金21,227元； 118年度每月租金美金21,864元； 119年度每月租金美金22,520元；租期60個月。 契約限制條款及其他重要約定事項：無 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 本次交易之決定方式：議價 價格決定之參考依據：市場價格 決策單位：經董事會決議授權由董事長先行決行，續提報最近期董事會追認 12.專業估價者事務所或公司名稱及其估價金額: 不適用 13.專業估價師姓名: 不適用 14.專業估價師開業證書字號: 不適用 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 業務營運使用 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:是 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |
| 20260709 | 2610 | 華航 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 坐落於633 Third Ave., Unit 8A, New York, NY 10017, USA之房舍 2.事實發生日:115/6/30~115/6/30 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:依『公開發行公司取得或處分資產處理準則』第15條第2項規定， 事後提報最近期董事會追認。 民國115年6月30日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 5,753平方英尺，交易總金額美金1,274,748元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：中美企業公司 與公司之關係：關係人(本公司之子公司) 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 選定關係人為交易對象之原因：地點符合營運需求 前次移轉情形：不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 每月初支付租金，115年度每月租金美金20,009元； 116年度每月租金美金20,609元； 117年度每月租金美金21,227元； 118年度每月租金美金21,864元； 119年度每月租金美金22,520元；租期60個月。 契約限制條款及其他重要約定事項：無 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 本次交易之決定方式：議價 價格決定之參考依據：市場價格 決策單位：經董事會決議授權由董事長先行決行，續提報最近期董事會追認 12.專業估價者事務所或公司名稱及其估價金額: 不適用 13.專業估價師姓名: 不適用 14.專業估價師開業證書字號: 不適用 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 業務營運使用 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:是 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2610 | 華航 | 8 | 5 | 5 | 8 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2610 | 華航 | 34 | 0 | 2813580.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
