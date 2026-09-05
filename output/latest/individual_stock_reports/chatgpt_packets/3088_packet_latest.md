# INDIVIDUAL STOCK CHATGPT PACKET - 3088 艾訊

## Metadata
- generated_at: 2026-09-05 15:53:11 Asia/Taipei
- stock_id: 3088
- stock_name: 艾訊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3088_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3088_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3088_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3088_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3088_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3088_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3088_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3088_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3088_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3088_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3088_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3088_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3088.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3088.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3088.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3088.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3088_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3088_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3088_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
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
- date: 20260904
- open: 123.5
- high: 128.5
- low: 123
- close: 127
- volume: 1551000
- ma5: 123.7
- ema23_primary: 127.36
- distance_to_ema23_pct: -0.28
- ma20: 128.1
- ma60: 134.82
- ma120: 122.62
- return_5d: 2.42
- return_20d: -6.96
- volume_ratio: 1.69
- distance_to_ma20_pct_auxiliary: -0.86
- distance_to_high_60_pct: -20.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,138,149.5,138,146,2969000,135.24,7.95,134.85,138.22,1.1
20260811,145.5,146,138,139.5,1894000,135.6,2.88,135.15,138.36,0.69
20260812,139.5,140.5,138,140,875000,135.96,2.97,135.2,138.53,0.32
20260813,141.5,141.5,138,138,787000,136.13,1.37,135.2,138.64,0.29
20260814,139.5,139.5,127.5,128.5,1859000,135.5,-5.16,135.18,138.53,0.66
20260817,128.5,129.5,125,127.5,880000,134.83,-5.44,135.25,138.37,0.31
20260818,129,129,125,127,734000,134.18,-5.35,134.68,138.12,0.26
20260819,126,128.5,124.5,126.5,621000,133.54,-5.27,133.62,137.88,0.25
20260820,128,128,124.5,125,591000,132.83,-5.89,132.18,137.59,0.27
20260821,125,125,123,124,424000,132.09,-6.13,130.85,137.25,0.22
20260824,124,126.5,124,125,428000,131.5,-4.94,130.03,137,0.23
20260825,126.5,126.5,122.5,124,508000,130.88,-5.25,129.6,136.72,0.29
20260826,125,126,123.5,125,669000,130.39,-4.13,129.18,136.44,0.4
20260827,126,126.5,123.5,123.5,558000,129.81,-4.86,129.32,136.15,0.38
20260828,125,126,123.5,124,409000,129.33,-4.12,129.62,135.88,0.32
20260831,124,124.5,122,123,477000,128.8,-4.5,129.65,135.62,0.41
20260901,123.5,127,121,125.5,958000,128.53,-2.35,129.75,135.4,0.84
20260902,126,126.5,123,123,401000,128.07,-3.96,129.28,135.29,0.4
20260903,124.5,124.5,120,120,761000,127.39,-5.8,128.57,135.03,0.82
20260904,123.5,128.5,123,127,1551000,127.36,-0.28,128.1,134.82,1.69
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 48.27
- over_600_ratio: 43.67
- over_800_ratio: 41.31
- over_1000_ratio: 37.34
- over_400_change_1w: -1.11
- over_800_change_1w: -0.51
- over_1000_change_1w: -0.47
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,48.53,-2.08,41.51,-0.85,38.23,-0.85,0,False,False
20260626,50.96,2.43,43.59,2.08,38.7,0.47,1,True,True
20260703,49.41,-1.55,43.94,0.35,38.37,-0.33,2,False,True
20260709,50.53,1.12,45.12,1.18,40.22,1.85,3,True,True
20260717,49.72,-0.81,44.14,-0.98,40.06,-0.16,0,False,False
20260724,51.67,1.95,44.58,0.44,40.5,0.44,1,True,True
20260731,50.27,-1.4,42.9,-1.68,38.9,-1.6,0,False,False
20260807,50.07,-0.2,43.93,1.03,39.9,1,1,False,True
20260814,50.5,0.43,43.78,-0.15,39.68,-0.22,2,False,False
20260821,49.36,-1.14,42.23,-1.55,38.14,-1.54,0,False,False
20260828,49.38,0.02,41.82,-0.41,37.81,-0.33,1,False,False
20260904,48.27,-1.11,41.31,-0.51,37.34,-0.47,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3088 | 艾訊 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:艾訊股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司國內第二次無擔保轉換公司債將於115年8月28日發行屆滿三年到期。 6.因應措施:債券到期時依債券面額以現金一次償還。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項): (1)本公司國內第二次無擔保轉換公司債將於115年8月28日到期，並於到期日之    次一營業日(115年8月31日)起終止上櫃買賣，依本公司國內第二次無擔保    轉換公司債發行及轉換辦法第六條規定，本公司於本轉換公司債到期時依    債券面額以現金一次償還。 (2)轉換辦理程序:債券持有人最遲應於到期日(115年8月28日)前向往來證券商辦理    轉換手續。 (3)到期還本辦理程序:本公司預計於115年9月11日以匯款或單掛號郵寄支票方式    予各債權人，郵費或匯費將自償還價款中扣除。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 3088 | 艾訊 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:艾訊股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司國內第二次無擔保轉換公司債將於115年8月28日發行屆滿三年到期。 6.因應措施:債券到期時依債券面額以現金一次償還。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項): (1)本公司國內第二次無擔保轉換公司債將於115年8月28日到期，並於到期日之    次一營業日(115年8月31日)起終止上櫃買賣，依本公司國內第二次無擔保    轉換公司債發行及轉換辦法第六條規定，本公司於本轉換公司債到期時依    債券面額以現金一次償還。 (2)轉換辦理程序:債券持有人最遲應於到期日(115年8月28日)前向往來證券商辦理    轉換手續。 (3)到期還本辦理程序:本公司預計於115年9月11日以匯款或單掛號郵寄支票方式    予各債權人，郵費或匯費將自償還價款中扣除。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 3088 | 艾訊 | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 51 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:艾訊股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司國內第二次無擔保轉換公司債將於115年8月28日發行屆滿三年到期。 6.因應措施:債券到期時依債券面額以現金一次償還。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項): (1)本公司國內第二次無擔保轉換公司債將於115年8月28日到期，並於到期日之    次一營業日(115年8月31日)起終止上櫃買賣，依本公司國內第二次無擔保    轉換公司債發行及轉換辦法第六條規定，本公司於本轉換公司債到期時依    債券面額以現金一次償還。 (2)轉換辦理程序:債券持有人最遲應於到期日(115年8月28日)前向往來證券商辦理    轉換手續。 (3)到期還本辦理程序:本公司預計於115年9月11日以匯款或單掛號郵寄支票方式    予各債權人，郵費或匯費將自償還價款中扣除。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3088 | 艾訊 | 1 | 1 | 1 | 1 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
