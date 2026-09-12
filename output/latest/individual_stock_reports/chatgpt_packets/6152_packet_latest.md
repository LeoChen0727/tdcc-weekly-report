# INDIVIDUAL STOCK CHATGPT PACKET - 6152 百一

## Metadata
- generated_at: 2026-09-12 15:44:12 Asia/Taipei
- stock_id: 6152
- stock_name: 百一
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6152_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6152_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6152_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6152_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6152_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6152_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6152_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6152_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6152_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6152_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6152_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6152_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6152.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6152.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6152.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6152.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6152_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6152_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6152_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260911
- open: 15.2
- high: 15.4
- low: 14.65
- close: 15
- volume: 2340189
- ma5: 14.38
- ema23_primary: 13.98
- distance_to_ema23_pct: 7.26
- ma20: 14.03
- ma60: 13.37
- ma120: 14.54
- return_5d: 8.7
- return_20d: 6.38
- volume_ratio: 2.4
- distance_to_ma20_pct_auxiliary: 6.91
- distance_to_high_60_pct: -9.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,13.9,14.4,13.9,14.2,1034868,13.36,6.32,12.8,13.73,0.74
20260818,14.15,14.35,13.8,13.8,742966,13.39,3.04,12.88,13.7,0.53
20260819,13.6,14.15,13.6,13.9,734139,13.44,3.46,12.96,13.67,0.51
20260820,14,14.15,13.75,13.95,519508,13.48,3.5,13.05,13.65,0.36
20260821,14.1,14.2,14,14.1,640473,13.53,4.21,13.14,13.63,0.44
20260824,14.1,14.15,13.75,13.75,567748,13.55,1.49,13.23,13.61,0.39
20260825,13.6,13.75,13.5,13.75,650726,13.57,1.36,13.32,13.59,0.45
20260826,13.7,14.1,13.7,14,591520,13.6,2.93,13.46,13.57,0.41
20260827,14.1,14.2,13.9,13.95,466114,13.63,2.34,13.61,13.54,0.32
20260828,14,14.2,13.9,14.05,684650,13.67,2.81,13.73,13.52,0.47
20260831,14.1,14.5,14,14.15,919893,13.71,3.24,13.85,13.5,0.62
20260901,14.15,14.15,13.8,13.8,665493,13.71,0.63,13.95,13.46,0.45
20260902,13.8,14.05,13.75,13.95,301703,13.73,1.58,14.05,13.44,0.2
20260903,13.95,14,13.55,13.55,491885,13.72,-1.23,14.13,13.42,0.33
20260904,13.8,13.8,13.6,13.8,319028,13.72,0.55,14.17,13.4,0.22
20260907,13.75,13.9,13.5,13.5,507388,13.71,-1.5,14.13,13.38,0.35
20260908,13.6,13.65,13.3,13.45,514532,13.68,-1.72,14.06,13.36,0.44
20260909,14.45,14.75,14.45,14.75,2203323,13.77,7.09,13.99,13.35,2.19
20260910,14,15.4,14,15.2,4618370,13.89,9.41,13.98,13.36,4.28
20260911,15.2,15.4,14.65,15,2340189,13.98,7.26,14.03,13.37,2.4
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 24.41
- over_600_ratio: 21.02
- over_800_ratio: 18.08
- over_1000_ratio: 15.91
- over_400_change_1w: 0.04
- over_800_change_1w: -0.58
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,24.45,0.64,19.07,0.03,16.98,0.02,6,True,True
20260703,24.76,0.31,19.09,0.02,16.98,0,7,False,True
20260709,24.56,-0.2,18.96,-0.13,16.85,-0.13,0,False,False
20260717,24.19,-0.37,17.97,-0.99,15.86,-0.99,0,False,False
20260724,23.88,-0.31,18.02,0.05,15.91,0.05,1,False,True
20260731,24.19,0.31,18.08,0.06,15.91,0,2,False,True
20260807,24.2,0.01,18.08,0,15.91,0,3,False,False
20260814,25.31,1.11,19.85,1.77,16.67,0.76,4,True,True
20260821,24.62,-0.69,19.14,-0.71,15.91,-0.76,0,False,False
20260828,24.74,0.12,19.66,0.52,15.91,0,1,False,True
20260904,24.37,-0.37,18.66,-1,15.91,0,0,False,False
20260911,24.41,0.04,18.08,-0.58,15.91,0,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 6152 | 百一 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  |  | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 土地：桃園市中壢區中工段602地號土地 建物：桃園市中壢區東園路69號廠房及附屬建物 2.事實發生日:115/6/17~115/6/17 3.董事會通過日期: 民國115年6月11日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 土地面積：4,030 平方公尺（約1219.075坪） 建物面積：2,449.32 平方公尺（約740.919坪） 交易總金額:新台幣505,000,000元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人:凱喬線路股份有限公司 與公司之關係：非關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 預計處分利益約383,000仟元。 實際處分利益將俟交易完成後，依成交價格扣除帳面價值、 土地增值稅、仲介費及相關交易成本後認列。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依雙方簽訂之不動產買賣契約約定辦理。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易決定方式：議價。 價格決定參考依據：專業估價報告、市場行情及雙方議價結果。 決策單位：經審計委員會同意及董事會決議授權董事長於授 權範圍內辦理。 12.專業估價者事務所或公司名稱及其估價金額: 估價機構：茗強不動產估價師事務所 估價金額：新台幣467,793,597元（未稅） 13.專業估價師姓名: 茗強不動產估價師事務所：蘇又德 14.專業估價師開業證書字號: (104)中市地估字第000083號（換發） 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 承湧不動產股份有限公司 經紀費用依委託銷售契約約定辦理。 23.取得或處分之具體目的或用途: 活化公司資產、提升資產使用效益及充實營運資金。 24.本次交易表示異議之董事之意見: 不適用 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 民國115年06月11日 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 115年6月17日 31.其他敘明事項: 本公司董事會於115年6月11日授權董事長於董事 會授權範圍內與潛在買方進行議價、協商並完成 正式買賣契約簽署，待後續產權移轉程序。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 6152 | 百一 | 3 | 3 | 3 | 3 | 4 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
