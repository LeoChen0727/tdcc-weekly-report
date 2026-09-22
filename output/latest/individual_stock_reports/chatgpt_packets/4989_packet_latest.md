# INDIVIDUAL STOCK CHATGPT PACKET - 4989 榮科

## Metadata
- generated_at: 2026-09-20 22:17:22 Asia/Taipei
- stock_id: 4989
- stock_name: 榮科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4989_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4989_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4989_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4989_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4989_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4989_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4989_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4989_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4989_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4989_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4989_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4989_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4989.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4989.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4989.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4989.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4989_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4989_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4989_latest.md?ref=main

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
- date: 20260918
- open: 60.9
- high: 61.8
- low: 60.3
- close: 61
- volume: 1871051
- ma5: 60.1
- ema23_primary: 62.42
- distance_to_ema23_pct: -2.27
- ma20: 62.21
- ma60: 69.96
- ma120: 81.22
- return_5d: 1.5
- return_20d: -1.45
- volume_ratio: 0.42
- distance_to_ma20_pct_auxiliary: -1.95
- distance_to_high_60_pct: -48.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,61.9,62.8,60.6,60.7,2021213,66.41,-8.6,63.13,78.58,0.28
20260825,60,61,58.8,60.9,2458885,65.95,-7.66,63.2,77.86,0.34
20260826,61.5,66.9,61.2,66.9,7774622,66.03,1.32,63.77,77.19,1.08
20260827,68.8,68.8,65.8,66.3,12459737,66.05,0.38,64.53,76.62,1.66
20260828,67.5,71.7,66.3,68.2,15471541,66.23,2.97,65.17,76.15,1.91
20260831,66.8,68.5,64.5,64.7,5652636,66.1,-2.12,65.34,75.69,0.71
20260901,65.1,68,64.7,64.7,5185141,65.99,-1.95,65.22,75.25,0.67
20260902,64,65.6,63.7,63.8,2895937,65.8,-3.05,65.06,74.93,0.42
20260903,64.3,65.6,60.4,60.5,4727679,65.36,-7.44,64.7,74.49,0.72
20260904,62.3,62.3,59.7,61.1,2536700,65.01,-6.01,64.47,74.14,0.4
20260907,62,62.7,60.9,61.8,2697045,64.74,-4.54,64.19,73.86,0.43
20260908,61.8,62.2,60.3,60.3,2454256,64.37,-6.32,63.8,73.53,0.42
20260909,61.2,61.9,60.9,61.5,1736758,64.13,-4.1,63.43,73.21,0.32
20260910,63.4,63.9,61.6,62.2,4872263,63.97,-2.77,63.08,72.94,0.94
20260911,60.8,61.6,60,60.1,2477255,63.65,-5.57,62.84,72.59,0.53
20260914,59,61.6,58.3,60,3185644,63.34,-5.28,62.6,72.17,0.68
20260915,59.8,60.7,58.3,58.3,2251477,62.92,-7.35,62.38,71.58,0.49
20260916,58.5,61.5,58.3,61.3,2313672,62.79,-2.37,62.36,71.03,0.52
20260917,61.6,62.5,59.9,59.9,3294222,62.55,-4.23,62.26,70.47,0.74
20260918,60.9,61.8,60.3,61,1871051,62.42,-2.27,62.21,69.96,0.42
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 17
- over_600_ratio: 14.76
- over_800_ratio: 12.72
- over_1000_ratio: 11.69
- over_400_change_1w: 0.09
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,30.1,7.05,25.52,5.73,23.62,5.68,2,True,True
20260709,33.85,3.75,30.35,4.83,29.03,5.41,3,True,True
20260717,26.32,-7.53,23.12,-7.23,20.44,-8.59,0,False,False
20260724,22.94,-3.38,17.29,-5.83,14.72,-5.72,0,False,False
20260731,36.75,13.81,31.81,14.52,31.25,16.53,1,True,True
20260807,19.41,-17.34,14.71,-17.1,12.53,-18.72,0,False,False
20260814,18.74,-0.67,13.86,-0.85,12.24,-0.29,0,False,False
20260821,18.34,-0.4,13.37,-0.49,12.27,0.03,1,False,True
20260828,18.38,0.04,14.02,0.65,12.91,0.64,2,True,True
20260904,17.88,-0.5,13.17,-0.85,12.19,-0.72,0,False,False
20260911,16.91,-0.97,12.7,-0.47,11.66,-0.53,0,False,False
20260918,17,0.09,12.72,0.02,11.69,0.03,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 4989 | 榮科 | revenue_pullback | 營收成長股價回檔 | 50.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/07/16 2.公司名稱:李長榮科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司現金增資發行新股認股繳款期限已於115年7月16日截止，依公司法 第142條、266條第3項規定，訂定自115年7月17日至115年8月17日下午3時30分止為尚未 繳款之原股東及認股員工之催告繳款期限。 6.因應措施: (1)尚未繳納股款之股東，請於上述期間內持原繳款書至中國信託營業部分行及 全國各地分行辦理繳款事宜，逾期未繳納者即喪失認購新股之權利。 (2)於催繳期間繳款之股東及員工，本公司將於催繳期間屆滿並經集保結算所作業後， 依所認購之股數，撥入所登記之集保帳號。 (3)若有任何疑問，請洽詢本公司股務代理機構：中國信託商業銀行代理部（地址： 台北市中正區重慶南路一段83號5樓，電話：02-6636-5566）。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 4989 | 榮科 | revenue_breakout_low_response | 營收爆發低反應股 | 15 | 41 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.事實發生日:115/07/16 2.公司名稱:李長榮科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司現金增資發行新股認股繳款期限已於115年7月16日截止，依公司法 第142條、266條第3項規定，訂定自115年7月17日至115年8月17日下午3時30分止為尚未 繳款之原股東及認股員工之催告繳款期限。 6.因應措施: (1)尚未繳納股款之股東，請於上述期間內持原繳款書至中國信託營業部分行及 全國各地分行辦理繳款事宜，逾期未繳納者即喪失認購新股之權利。 (2)於催繳期間繳款之股東及員工，本公司將於催繳期間屆滿並經集保結算所作業後， 依所認購之股數，撥入所登記之集保帳號。 (3)若有任何疑問，請洽詢本公司股務代理機構：中國信託商業銀行代理部（地址： 台北市中正區重慶南路一段83號5樓，電話：02-6636-5566）。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 4989 | 榮科 | 23 | 13 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 4989 | 榮科 | 10 | 0 | 4500.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
