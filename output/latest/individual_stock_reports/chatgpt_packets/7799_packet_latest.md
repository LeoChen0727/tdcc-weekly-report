# INDIVIDUAL STOCK CHATGPT PACKET - 7799 禾榮科

## Metadata
- generated_at: 2026-07-06 22:28:16 Asia/Taipei
- stock_id: 7799
- stock_name: 禾榮科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260706
- price_rows: 189
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/7799_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/7799_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7799.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7799.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7799.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7799.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7799_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7799_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7799_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260706
- open: 405
- high: 430
- low: 405
- close: 430
- volume: 1084000
- ma5: 404.9
- ema23_primary: 382.44
- distance_to_ema23_pct: 12.44
- ma20: 381.27
- ma60: 362.73
- ma120: 395.01
- return_5d: 3.24
- return_20d: 10.26
- volume_ratio: 1.3
- distance_to_ma20_pct_auxiliary: 12.78
- distance_to_high_60_pct: -5.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260608,359,408,359,377.5,1519199,343.24,9.98,329.23,363.69,3.3
20260609,376.5,388,362.5,364,925773,344.97,5.52,330.8,362.56,1.87
20260610,364,366,338.5,340.5,647367,344.6,-1.19,331.4,361.23,1.25
20260611,340.5,342,329,334.5,286720,343.76,-2.69,332.02,359.93,0.55
20260612,335.5,348,335.5,346,255553,343.94,0.6,334.07,358.7,0.5
20260615,352.5,357,350,352,230898,344.61,2.14,336.15,357.61,0.46
20260616,361,378.5,355.5,355.5,667268,345.52,2.89,338.77,356.73,1.28
20260617,353.5,361,350.5,357,160327,346.48,3.04,341.27,355.84,0.31
20260618,358.5,373,358,362,964303,347.77,4.09,343.52,355.28,1.72
20260622,362.5,393.5,359,386,885365,350.96,9.98,346.4,355.17,1.49
20260623,388,424.5,386,424.5,1249324,357.09,18.88,350.7,355.75,1.97
20260624,430,453,408,413,2457243,361.75,14.17,354.93,356.17,3.32
20260625,409.5,416,391.5,393,764796,364.35,7.86,358.48,356.17,1
20260626,393,401.5,378,379,546701,365.57,3.67,361.38,356.53,0.71
20260629,385.5,416.5,381.5,416.5,831462,369.81,12.62,366.3,358,1.04
20260630,408.5,432.5,408.5,410,1289000,373.16,9.87,370.3,359.03,1.53
20260701,414,416.5,395.5,395.5,491000,375.02,5.46,373.77,359.94,0.57
20260702,406.5,415,394.5,398,535000,376.94,5.59,377.5,361.04,0.61
20260703,399.5,415.5,390,391,853651,378.11,3.41,379.27,361.76,0.97
20260706,405,430,405,430,1084000,382.44,12.44,381.27,362.73,1.3
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 79.46
- over_600_ratio: 75.13
- over_800_ratio: 74.69
- over_1000_ratio: 71.77
- over_400_change_1w: -0.08
- over_800_change_1w: -0.06
- over_1000_change_1w: -0.05
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.16,,74.77,,71.19,,0,False,False
20260508,80.12,-0.04,74.77,0,71.19,0,0,False,False
20260515,80.46,0.34,74.77,0,71.19,0,1,False,False
20260522,80.34,-0.12,74.77,0,71.19,0,0,False,False
20260529,80.39,0.05,74.77,0,71.19,0,1,False,False
20260605,80.34,-0.05,74.74,-0.03,71.8,0.61,2,False,True
20260612,80.18,-0.16,74.77,0.03,71.83,0.03,3,False,True
20260618,80.26,0.08,74.77,0,71.83,0,4,False,False
20260626,79.54,-0.72,74.75,-0.02,71.82,-0.01,0,False,False
20260703,79.46,-0.08,74.69,-0.06,71.77,-0.05,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 7799 | 禾榮科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 68.0 |  |  | platform_right_side |  |  | repeated_but_no_breakout | 1.事實發生日:115/06/25 2.契約或承諾相對人:B dot Medical Inc. 3.與公司關係:無 4.契約或承諾起迄日期（或解除日期）:115/06/25 5.主要內容（解除者不適用）: 本公司與B dot Medical Inc.簽署合作意向書，雙方將針對AB-BNCT系統日本市場拓展、 潛在粒子治療中心建置、醫療設備技術整合及日本市場法規與取證支援之合作可行性 展開進一步評估。此合作藉由雙方於先進粒子醫療領域之技術與市場互補，共同開拓 日本及亞洲醫療市場。 6.限制條款（解除者不適用）:無 7.承諾事項（解除者不適用）:無 8.其他重要約定事項（解除者不適用）:無 9.對公司財務、業務之影響: 此合作有助於本公司持續以穩健方式深化海外布局，推動公司業務拓展與長期成長。 10.具體目的: 擴展本公司在AB-BNCT領域之潛在市場發展。 11.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第8款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 7799 | 禾榮科 | 1 | 1 | 2 | 4 | 5 | repeated_but_no_breakout | 近 10 日上榜 4 次、近 20 日上榜 5 次，但尚未有效突破，需等待攻擊確認。 |

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
