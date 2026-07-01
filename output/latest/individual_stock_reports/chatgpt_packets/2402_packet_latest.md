# INDIVIDUAL STOCK CHATGPT PACKET - 2402 毅嘉

## Metadata
- generated_at: 2026-07-01 22:27:11 Asia/Taipei
- stock_id: 2402
- stock_name: 毅嘉
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 295
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2402_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2402_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2402_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2402_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2402_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2402_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2402_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2402_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2402_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2402_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2402_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2402_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2402.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2402.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2402.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2402.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2402_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2402_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2402_latest.md?ref=main

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
- date: 20260701
- open: 65.7
- high: 67.8
- low: 63.8
- close: 67.1
- volume: 3501000
- ma5: 65.44
- ema23_primary: 66.81
- distance_to_ema23_pct: 0.44
- ma20: 66.67
- ma60: 67.7
- ma120: 61.06
- return_5d: -0.74
- return_20d: -2.33
- volume_ratio: 0.46
- distance_to_ma20_pct_auxiliary: 0.65
- distance_to_high_60_pct: -21.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,69.1,72.5,69.1,69.7,18391338,67.58,3.14,67.27,62.75,1.87
20260604,69.7,70.3,68.2,69.3,8602360,67.72,2.33,67.23,63.12,0.87
20260605,68.9,69,65.6,66.3,7255287,67.61,-1.93,67.14,63.39,0.74
20260608,59.8,63.9,59.7,63.5,6098512,67.26,-5.59,66.87,63.59,0.62
20260609,63.6,64.5,62.6,63.8,3949462,66.97,-4.74,66.52,63.82,0.43
20260610,63,64.5,59.7,59.7,5577470,66.37,-10.05,66.11,63.96,0.62
20260611,60,61.1,57.6,60.6,5121913,65.89,-8.03,65.74,64.12,0.57
20260612,62.2,66.6,62.1,66.6,9410428,65.95,0.99,65.88,64.39,1.05
20260615,67.6,70.4,67.5,68.5,10350167,66.16,3.54,66.1,64.69,1.12
20260616,68.7,71.4,67.3,70,10258659,66.48,5.3,66.44,64.99,1.07
20260617,71.5,71.7,69.5,70.9,23446988,66.85,6.06,66.89,65.32,2.23
20260618,70.9,71,69.3,70,7794800,67.11,4.31,67.28,65.66,0.73
20260622,70.8,72.3,70,71.3,11933100,67.46,5.69,67.55,66,1.09
20260623,71.6,71.7,67.9,68.3,7909655,67.53,1.14,67.57,66.28,0.74
20260624,67.4,68.9,67.2,67.6,3443227,67.54,0.1,67.44,66.56,0.36
20260625,68.4,68.4,66.8,66.9,2873245,67.48,-0.86,67.36,66.79,0.32
20260626,66.7,67.4,63.9,64.1,3797458,67.2,-4.61,67.25,66.99,0.43
20260629,64.9,65.9,63.4,64.3,2146484,66.96,-3.97,67,67.24,0.26
20260630,64.8,66.1,64.5,64.8,1817000,66.78,-2.96,66.75,67.46,0.23
20260701,65.7,67.8,63.8,67.1,3501000,66.81,0.44,66.67,67.7,0.46
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 38.53
- over_600_ratio: 36.35
- over_800_ratio: 35.66
- over_1000_ratio: 34.21
- over_400_change_1w: 0.01
- over_800_change_1w: -0.09
- over_1000_change_1w: -0.37
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.64,,43.47,,41.66,,0,False,False
20260508,46.02,-1.62,42.5,-0.97,41.58,-0.08,0,False,False
20260515,45.44,-0.58,41.99,-0.51,41.11,-0.47,0,False,False
20260522,45.51,0.07,41.98,-0.01,40,-1.11,1,False,False
20260529,39.58,-5.93,36.1,-5.88,34.29,-5.71,0,False,False
20260605,39.48,-0.1,36.08,-0.02,34.62,0.33,1,False,True
20260612,38.35,-1.13,35.61,-0.47,34.46,-0.16,0,False,False
20260618,38.52,0.17,35.75,0.14,34.58,0.12,1,False,True
20260626,38.53,0.01,35.66,-0.09,34.21,-0.37,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2402 | 毅嘉 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  | call_inflow | stale_signal | 1.股東會決議日:115/06/16 2.許可從事競業行為之董事姓名及職稱:  董事:黃秋永、黃麗玲、黃子軒、曾恭勝  獨立董事:許萬龍、徐豫東、劉致宏 3.許可從事競業行為之項目:與本公司營業範圍相同或類似之公司 4.許可從事競業行為之期間:任職本公司董事之職務期間 5.決議情形（請依公司法第209條說明表決結果）:經票決結果， 贊成權數：188,264,843權，佔出席股東表決總權數85.77%； 反對權數：1,178,828權；無效權數：0權；棄權/未投票權數： 30,046,187權；贊成權數超過法定數額，本案照案通過。 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:獨立董事:徐豫東 董事:黃秋永、黃麗玲、曾恭勝 7.所擔任該大陸地區事業之公司名稱及職務: ICHIA HOLDINGS (H.K) CO., LTD董事長-黃秋永、董事-黃麗玲 毅嘉電子(蘇州)有限公司董事長兼總經理-曾恭勝、董事-黃麗玲 中山毅永電子有限公司董事長兼總經理-曾恭勝、董事-黃麗玲 晶鴻微電子(上海)有限公司董事長-徐豫東 東莞晶宏半導體有限公司董事長-徐豫東 8.所擔任該大陸地區事業地址: ICHIA HOLDINGS (H.K) CO., LTD-香港灣仔告士打道151號國衛中心1004室 毅嘉電子(蘇州)有限公司-江蘇省蘇州市蘇州新區金山路118號 中山毅永電子有限公司-廣東省中山市張家邊火炬開發區逸仙路26號 晶鴻微電子(上海)有限公司-上海市徐匯區桂平路481號15號樓3樓 東莞晶宏半導體有限公司-廣東省東莞市松山湖園區總部二路2號1棟1單元808室 9.所擔任該大陸地區事業營業項目: ICHIA HOLDINGS (H.K) CO., LTD-各項投資業務 毅嘉電子(蘇州)有限公司-橡膠、塑膠按鍵及軟性印刷電路板製造、銷售 中山毅永電子有限公司-各種電子、通訊(信)及電腦之各種電子零組件及其材料之製造 、加工及買賣業務 晶鴻微電子(上海)有限公司-IC銷售及售後服務 東莞晶宏半導體有限公司-IC研發、銷售及售後服務 10.對本公司財務業務之影響程度:無重大影響 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:無 12.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2402 | 毅嘉 | 1 | 1 | 1 | 4 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2402 | 毅嘉 | 90 | 9 | 6836430.0 | 640860.0 | 10.67 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
