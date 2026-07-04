# INDIVIDUAL STOCK CHATGPT PACKET - 2340 台亞

## Metadata
- generated_at: 2026-07-04 22:26:26 Asia/Taipei
- stock_id: 2340
- stock_name: 台亞
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2340_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2340_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2340_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2340_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2340_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2340_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2340_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2340_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2340_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2340_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2340_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2340_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2340.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2340.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2340.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2340.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2340_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2340_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2340_latest.md?ref=main

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
- date: 20260703
- open: 39
- high: 40.35
- low: 37.2
- close: 38.1
- volume: 11939875
- ma5: 37.03
- ema23_primary: 37.65
- distance_to_ema23_pct: 1.2
- ma20: 37.35
- ma60: 36.66
- ma120: 31.74
- return_5d: 4.53
- return_20d: 2.7
- volume_ratio: 0.99
- distance_to_ma20_pct_auxiliary: 2
- distance_to_high_60_pct: -16.99

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260605,37.1,37.1,34.7,35.65,4443323,36.74,-2.96,36.82,33.47,0.56
20260608,32.1,32.85,32.1,32.7,4812074,36.4,-10.16,36.59,33.59,0.62
20260609,33.1,35.4,31.9,35,7717153,36.28,-3.54,36.44,33.73,0.98
20260610,34.05,35.3,32.75,32.75,5240743,35.99,-9,36.27,33.82,0.68
20260611,31.6,33.3,31.25,33.05,3480655,35.74,-7.54,36.11,33.9,0.46
20260612,33.7,36,33.7,34.6,4586261,35.65,-2.94,36.1,33.98,0.61
20260615,35.5,37.3,35.3,36.6,6710972,35.73,2.44,36.19,34.11,0.89
20260616,37.3,40.25,37,39.1,27123349,36.01,8.59,36.44,34.29,3.1
20260617,39.2,39.95,38.15,38.5,16451826,36.22,6.31,36.65,34.45,1.76
20260618,38.8,41.95,38.8,39.95,19977197,36.53,9.37,36.88,34.64,1.97
20260622,42.15,43.85,42,42.8,22297392,37.05,15.52,37.09,34.89,2.08
20260623,42.9,45.8,42.45,43.55,30420814,37.59,15.85,37.28,35.14,2.71
20260624,42.7,44.55,41.55,42,16333916,37.96,10.65,37.44,35.38,1.4
20260625,42.45,42.7,38.95,39.2,13601079,38.06,2.99,37.39,35.59,1.17
20260626,39,40.25,36.25,36.45,11975717,37.93,-3.9,37.31,35.77,1.03
20260629,36.4,36.95,35.2,35.7,6723729,37.74,-5.41,37.19,35.96,0.58
20260630,36.5,38.5,36.4,37.55,6156000,37.73,-0.47,37.23,36.17,0.53
20260701,38.5,39.25,35,35.15,8492000,37.51,-6.3,37.23,36.32,0.73
20260702,35.4,38.65,35.3,38.65,13027000,37.61,2.77,37.3,36.51,1.1
20260703,39,40.35,37.2,38.1,11939875,37.65,1.2,37.35,36.66,0.99
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 39.54
- over_600_ratio: 37.4
- over_800_ratio: 36.02
- over_1000_ratio: 34.61
- over_400_change_1w: -0.91
- over_800_change_1w: -1.17
- over_1000_change_1w: -1.38
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,39.31,,35.26,,33.27,,0,False,False
20260508,37.22,-2.09,33.89,-1.37,32.47,-0.8,0,False,False
20260515,37.26,0.04,33.5,-0.39,32.27,-0.2,1,False,False
20260522,37.33,0.07,33.52,0.02,32.27,0,2,False,True
20260529,38.01,0.68,34.63,1.11,32.98,0.71,3,True,True
20260605,37.87,-0.14,34.26,-0.37,32.82,-0.16,0,False,False
20260612,37.3,-0.57,32.57,-1.69,31.33,-1.49,0,False,False
20260618,38.3,1,34.45,1.88,32.83,1.5,1,True,True
20260626,40.45,2.15,37.19,2.74,35.99,3.16,2,True,True
20260703,39.54,-0.91,36.02,-1.17,34.61,-1.38,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 2340 | 台亞 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_strong_inflow | stale_signal | 1.事實發生日:115/07/01 2.公司名稱:台亞半導體股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:週刊王 6.報導內容: 115/07/01 CTWant週刊王報導：德勝光電2022年間向知名 科技大廠台亞半導體採購，...台亞多次通知德勝應給付 210萬元的貨款，卻遭對方拒絕，更拒絕受領7500個已 製成之產品。...等內容。 7.發生緣由: 1.德勝光電股份有限公司（以下簡稱 德勝光電）於民國111年間 與本公司簽訂採購單，訂購特殊規格基板之封裝品，本公司已 依約完成，惟德勝光電因惡意違約，拒絕受領並未支付貨款。 2.本案業經臺灣桃園地方法民事判決，就部分已履行之交易價款 及相關損害賠償請求作成判決。 8.因應措施: 1.本公司已自 113 年啟動追償貨款及請求損害賠償，經起訴 審理後，本公司於114年底取得一審全面勝訴判決且全案已確定。 2.目前案件已全面進入強制執行與財產查扣階段，正積極 透過律師進行最終債權回收程序中。 3.本案不影響本公司銷售之業務，對本公司財務業務無重大影響。 9.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 2340 | 台亞 | 2 | 2 | 3 | 7 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 2340 | 台亞 | 23 | 0 | 5438590.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
