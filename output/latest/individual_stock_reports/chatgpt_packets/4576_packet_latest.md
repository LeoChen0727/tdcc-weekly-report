# INDIVIDUAL STOCK CHATGPT PACKET - 4576 大銀微系統

## Metadata
- generated_at: 2026-09-05 22:16:57 Asia/Taipei
- stock_id: 4576
- stock_name: 大銀微系統
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4576_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4576_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4576_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4576_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4576_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4576_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4576_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4576_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4576_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4576_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4576_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4576_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4576.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4576.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4576.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4576.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4576_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4576_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4576_latest.md?ref=main

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
- date: 20260904
- open: 236
- high: 239.5
- low: 223
- close: 238
- volume: 3520267
- ma5: 231.6
- ema23_primary: 217.12
- distance_to_ema23_pct: 9.62
- ma20: 217.95
- ma60: 210.49
- ma120: 204.95
- return_5d: 10.19
- return_20d: 9.17
- volume_ratio: 1.22
- distance_to_ma20_pct_auxiliary: 9.2
- distance_to_high_60_pct: -5.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,223.5,232.5,214.5,226.5,3149130,204.47,10.77,197.88,219.73,1.74
20260811,223.5,226,216,218.5,1684823,205.64,6.25,198.68,218.95,0.94
20260812,217,231,217,227,2231864,207.42,9.44,199.72,218.43,1.2
20260813,228,235.5,222.5,224,4165130,208.8,7.28,200.38,217.96,2.06
20260814,224,226.5,217.5,221,1287472,209.82,5.33,201.72,217.7,0.64
20260817,220,233,220,225.5,2760470,211.12,6.81,203.62,217.32,1.32
20260818,223.5,226.5,209,210.5,1617769,211.07,-0.27,204.6,216.47,0.76
20260819,206.5,219,205,208,1528579,210.82,-1.34,205.1,215.32,0.71
20260820,213,228.5,206.5,208,5311189,210.58,-1.23,205.55,214.05,2.22
20260821,208,208.5,199,202.5,1584800,209.91,-3.53,206.1,212.88,0.65
20260824,207,207,198,198,1011856,208.92,-5.22,206.18,211.92,0.41
20260825,197.5,197.5,190.5,197,1048318,207.92,-5.25,207,210.76,0.42
20260826,199,204,195.5,203,1034928,207.51,-2.17,208.35,209.76,0.43
20260827,204,220.5,204,215.5,2595106,208.18,3.52,210.9,209.38,1.06
20260828,220.5,223,208.5,216,1949063,208.83,3.43,212.68,209.1,0.78
20260831,211,219.5,208.5,216.5,1246830,209.47,3.36,213.65,208.89,0.5
20260901,215,237,215,230.5,3703735,211.22,9.13,215.12,209.06,1.42
20260902,229,252,227.5,242,7351242,213.79,13.2,216.32,209.59,2.6
20260903,250,251.5,229.5,231,9012781,215.22,7.33,216.95,209.88,2.9
20260904,236,239.5,223,238,3520267,217.12,9.62,217.95,210.49,1.22
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 67.75
- over_600_ratio: 66.46
- over_800_ratio: 63.47
- over_1000_ratio: 59.69
- over_400_change_1w: 1.28
- over_800_change_1w: 2.6
- over_1000_change_1w: 1.05
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,65.64,-0.87,62.83,-0.3,59.9,-0.22,0,False,False
20260626,66.06,0.42,63.91,1.08,60.86,0.96,1,True,True
20260703,66.47,0.41,63.58,-0.33,61.23,0.37,2,False,True
20260709,65.32,-1.15,62.5,-1.08,59.32,-1.91,0,False,False
20260717,65.64,0.32,62.86,0.36,60.49,1.17,1,True,True
20260724,65.55,-0.09,61.67,-1.19,59.38,-1.11,0,False,False
20260731,65.75,0.2,61.86,0.19,60.32,0.94,1,True,True
20260807,66.74,0.99,62.47,0.61,59.49,-0.83,2,False,True
20260814,66.88,0.14,63.14,0.67,59.41,-0.08,3,False,True
20260821,66.32,-0.56,60.82,-2.32,58.58,-0.83,0,False,False
20260828,66.47,0.15,60.87,0.05,58.64,0.06,1,True,True
20260904,67.75,1.28,63.47,2.6,59.69,1.05,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4576 | 大銀微系統 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/09/03 2.公司名稱:大銀微系統股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:經濟日報 6.報導內容: 『…法人估…大銀8月營收有機會突破4億元大關…全年合併營收將可進一步突破 40億元大關，…』 7.發生緣由: 關於上述報導，係媒體及法人推測並非本公司發佈之訊息，謹此澄清。有關本公司 之財務及業務資訊，皆以公開資訊觀測站公告為主，特此說明。 8.因應措施:無 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 4576 | 大銀微系統 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/09/03 2.公司名稱:大銀微系統股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:經濟日報 6.報導內容: 『…法人估…大銀8月營收有機會突破4億元大關…全年合併營收將可進一步突破 40億元大關，…』 7.發生緣由: 關於上述報導，係媒體及法人推測並非本公司發佈之訊息，謹此澄清。有關本公司 之財務及業務資訊，皆以公開資訊觀測站公告為主，特此說明。 8.因應措施:無 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 4576 | 大銀微系統 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/09/03 2.公司名稱:大銀微系統股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:經濟日報 6.報導內容: 『…法人估…大銀8月營收有機會突破4億元大關…全年合併營收將可進一步突破 40億元大關，…』 7.發生緣由: 關於上述報導，係媒體及法人推測並非本公司發佈之訊息，謹此澄清。有關本公司 之財務及業務資訊，皆以公開資訊觀測站公告為主，特此說明。 8.因應措施:無 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4576 | 大銀微系統 | 14 | 2 | 5 | 10 | 17 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 17 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4576 | 大銀微系統 | 73 | 0 | 11334800.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
