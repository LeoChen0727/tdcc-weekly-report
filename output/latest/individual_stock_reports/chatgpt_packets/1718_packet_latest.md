# INDIVIDUAL STOCK CHATGPT PACKET - 1718 中纖

## Metadata
- generated_at: 2026-07-05 22:26:17 Asia/Taipei
- stock_id: 1718
- stock_name: 中纖
- packet_status: standard_180d_window_packet
- latest_price_date: 20260703
- price_rows: 297
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1718_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1718_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1718.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1718.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1718.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1718.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1718_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1718_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1718_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_confirmed
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
- model_recommended
- decision_score_high
- price_structure_not_broken
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260703
- open: 14.25
- high: 14.95
- low: 14.1
- close: 14.95
- volume: 148912446
- ma5: 13.33
- ema23_primary: 10.57
- distance_to_ema23_pct: 41.45
- ma20: 10.54
- ma60: 8.07
- ma120: 7.65
- return_5d: 34.08
- return_20d: 54.44
- volume_ratio: 2.39
- distance_to_ma20_pct_auxiliary: 41.87
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260605,9.89,10.2,8.72,9.85,205424843,7.36,33.87,7.05,7.1,10.6
20260608,9.37,10.2,9,10,32120210,7.58,31.96,7.22,7.14,1.54
20260609,10.25,10.75,9.21,9.41,39528263,7.73,21.72,7.36,7.17,1.76
20260610,9.41,9.41,8.85,8.9,17099937,7.83,13.69,7.48,7.19,0.74
20260611,8.9,9.1,8.9,9.05,9217814,7.93,14.12,7.59,7.22,0.4
20260612,9.39,9.42,9.18,9.2,7071869,8.04,14.49,7.74,7.25,0.3
20260615,9.36,9.36,9.11,9.28,8491703,8.14,14.01,7.87,7.28,0.36
20260616,9.35,9.35,9.21,9.21,5332578,8.23,11.93,8.01,7.31,0.23
20260617,9.25,9.87,9.25,9.79,13159965,8.36,17.12,8.18,7.34,0.54
20260618,10.1,10.1,9.53,9.86,14075596,8.48,16.22,8.34,7.38,0.57
20260622,10,10,9.74,9.78,13806893,8.59,13.83,8.51,7.41,0.54
20260623,9.78,9.79,9.03,9.25,26146079,8.65,6.98,8.65,7.44,0.99
20260624,9.04,9.41,8.96,9.23,16068258,8.7,6.15,8.79,7.47,0.59
20260625,9.29,10.15,9.29,10.15,54273393,8.82,15.12,8.99,7.52,1.84
20260626,10.35,11.15,9.93,11.15,153432821,9.01,23.74,9.22,7.57,4.14
20260629,11.85,12.25,11.85,12.25,33754509,9.28,31.99,9.51,7.65,0.88
20260630,12.95,13.45,12.5,13.45,91732000,9.63,39.69,9.81,7.75,2.18
20260701,14.35,14.5,12.15,12.4,291800000,9.86,25.77,10.03,7.84,5.38
20260702,12.6,13.6,12.55,13.6,63424000,10.17,33.71,10.27,7.94,1.12
20260703,14.25,14.95,14.1,14.95,148912446,10.57,41.45,10.54,8.07,2.39
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 55.16
- over_600_ratio: 52.95
- over_800_ratio: 51.62
- over_1000_ratio: 50.4
- over_400_change_1w: -1.01
- over_800_change_1w: -0.61
- over_1000_change_1w: -0.89
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.68,,51.2,,49.68,,0,False,False
20260508,55.7,0.02,51.18,-0.02,49.67,-0.01,1,False,False
20260515,55.88,0.18,51.38,0.2,50.03,0.36,2,True,True
20260522,55.83,-0.05,51.33,-0.05,49.88,-0.15,0,False,False
20260529,55.86,0.03,51.21,-0.12,49.76,-0.12,1,False,False
20260605,57.16,1.3,52.67,1.46,51.38,1.62,2,True,True
20260612,54.66,-2.5,50.62,-2.05,49.45,-1.93,0,False,False
20260618,54.91,0.25,50.91,0.29,49.8,0.35,1,True,True
20260626,56.17,1.26,52.23,1.32,51.29,1.49,2,True,True
20260703,55.16,-1.01,51.62,-0.61,50.4,-0.89,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 1718 | 中纖 | true_breakout | 嚴格突破 | 91.0 |  |  | breakout_confirmed |  | call_inflow | continued_overheated | 1.證券名稱: 台中商業銀行股份有限公司普通股 2.交易日期:115/4/24~115/6/29 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年4月22日 5.交易數量、每單位價格及交易總金額: 交易數量：19,753,570股 每單位價格：平均約19.39元 交易總金額：382,926,229元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益約228,010仟元 7.與交易標的公司之關係: 台中銀為母公司中纖採權益法評價之投資公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 中纖:1,277,768,406股，20,269,770,990元，21.22％，質押592,060仟股 磐亞:341,322,463股，5,414,493,303元，5.63％，無質押情形 德興投資:17,650,648股，275,487,211元，0.29％，質押4,500仟股 久津實業:10,354,498股，212,784,934元，0.17％，質押9,175仟股 久暢:0股，0元，0％，無質押情形 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 0.74％，1.34％，213,965,015元 10.取得或處分之具體目的: 實現利益 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 不適用，原因:董事長核決 115年4月22日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 本次交易依取得成本計算，處分利益約為新台幣228,010仟元，惟依IFRS9 規定，本年度實際可認列之損益金額，以本公司經會計師查核或核閱；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 1718 | 中纖 | 6 | 1 | 5 | 6 | 11 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 1718 | 中纖 | 9 | 0 | 4463730.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
