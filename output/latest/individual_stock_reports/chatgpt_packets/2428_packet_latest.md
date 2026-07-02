# INDIVIDUAL STOCK CHATGPT PACKET - 2428 興勤

## Metadata
- generated_at: 2026-07-02 22:26:34 Asia/Taipei
- stock_id: 2428
- stock_name: 興勤
- packet_status: standard_180d_window_packet
- latest_price_date: 20260702
- price_rows: 296
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2428_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2428_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2428.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2428.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2428.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2428.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2428_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2428_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2428_latest.md?ref=main

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
- date: 20260702
- open: 300
- high: 313
- low: 299.5
- close: 311
- volume: 1712000
- ma5: 304.9
- ema23_primary: 289.72
- distance_to_ema23_pct: 7.35
- ma20: 296.07
- ma60: 236.14
- ma120: 202.76
- return_5d: 0.97
- return_20d: 14.76
- volume_ratio: 0.63
- distance_to_ma20_pct_auxiliary: 5.04
- distance_to_high_60_pct: -6.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260604,268,270.5,262,265,1040118,239.78,10.52,238.6,191.79,0.37
20260605,263,287,257,283,3351311,243.38,16.28,243.22,193.75,1.21
20260608,255.5,277.5,255.5,272.5,2079971,245.81,10.86,247.2,195.6,0.75
20260609,278.5,292,271.5,289,3729811,249.41,15.88,251.57,197.78,1.32
20260610,283,307,283,286,7506305,252.46,13.29,255.72,199.88,2.4
20260611,279.5,291.5,272,281,3459999,254.83,10.27,259.18,201.9,1.1
20260612,294.5,302,286.5,291,2672919,257.85,12.86,263.43,204.01,0.86
20260615,296.5,319,296.5,310,3352084,262.19,18.23,268.35,206.43,1.04
20260616,310,312.5,279,280,3478986,263.68,6.19,271.65,208.39,1.05
20260617,279.5,300,279,299,2101680,266.62,12.14,275.45,210.69,0.65
20260618,299,322,299,316,3696697,270.74,16.72,279.75,213.38,1.13
20260622,319,320,303,311,2609487,274.09,13.47,283.18,216,0.79
20260623,311,313.5,300.5,301.5,1778667,276.38,9.09,286.1,218.39,0.54
20260624,295.5,304.5,295,304,1441043,278.68,9.09,288.5,220.83,0.45
20260625,305,313.5,300.5,308,2336846,281.12,9.56,290.6,223.34,0.74
20260626,310,312.5,295,296.5,1652235,282.4,4.99,290.8,225.72,0.53
20260629,301,305,294,298,816271,283.7,5.04,291.1,228.2,0.29
20260630,302,318,300.5,315,2583000,286.31,10.02,292.7,230.86,0.95
20260701,319,334,303,304,2872000,287.78,5.63,294.07,233.43,1.06
20260702,300,313,299.5,311,1712000,289.72,7.35,296.07,236.14,0.63
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 64.15
- over_600_ratio: 60.86
- over_800_ratio: 56.05
- over_1000_ratio: 52.55
- over_400_change_1w: -0.33
- over_800_change_1w: -0.43
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.56,,52.71,,49.97,,0,False,False
20260508,61.01,0.45,54.13,1.42,49.97,0,1,False,True
20260515,62.57,1.56,54.78,0.65,50.78,0.81,2,True,True
20260522,64.32,1.75,54.93,0.15,50.86,0.08,3,True,True
20260529,65.1,0.78,56.54,1.61,52.62,1.76,4,True,True
20260605,64.51,-0.59,55.94,-0.6,51.88,-0.74,0,False,False
20260612,63.81,-0.7,56.6,0.66,51.91,0.03,1,False,True
20260618,64.48,0.67,56.48,-0.12,52.45,0.54,2,False,True
20260626,64.15,-0.33,56.05,-0.43,52.55,0.1,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 2428 | 興勤 | pattern | 型態觀察 | 46.0 |  |  | base_building |  | no_signal | stale_signal | 1.事實發生日:115/07/01 2.接受資金貸與之: (1)公司名稱:為勤電子有限公司 (2)與資金貸與他人公司之關係: 直接持有100%之子公司 (3)資金貸與之限額(仟元):1,181,491 (4)原資金貸與之餘額(仟元):422,010 (5)本次新增資金貸與之金額(仟元):656,460 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):1,078,470 (8)本次新增資金貸與之原因: 營運週轉需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):693,600 (2)累積盈虧金額(仟元):313,327 5.計息方式: 2.5% 6.還款之: (1)條件: 依合約規定 (2)日期: 依合約規定 7.迄事實發生日為止，資金貸與餘額(仟元): 1,078,470 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 9.18 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 新增資金貸與金額為人民幣140,000元，依115/07/01台銀買進賣出即期平均匯率4.689， 折合新台幣為656,460仟元。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 2428 | 興勤 | 3 | 3 | 4 | 7 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 2428 | 興勤 | 29 | 0 | 10044620.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
