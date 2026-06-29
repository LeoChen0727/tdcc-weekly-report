# INDIVIDUAL STOCK CHATGPT PACKET - 6472 保瑞

## Metadata
- generated_at: 2026-06-29 22:27:44 Asia/Taipei
- stock_id: 6472
- stock_name: 保瑞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260629
- price_rows: 293
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6472_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6472_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6472_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6472_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6472_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6472_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6472_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6472_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6472_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6472_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6472_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6472_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6472.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6472.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6472.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6472.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6472_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6472_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6472_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260629
- open: 419
- high: 453
- low: 419
- close: 437.5
- volume: 3026054
- ma5: 430.4
- ema23_primary: 405.36
- distance_to_ema23_pct: 7.93
- ma20: 398.52
- ma60: 399.76
- ma120: 453.52
- return_5d: 3.43
- return_20d: 26.45
- volume_ratio: 1.78
- distance_to_ma20_pct_auxiliary: 9.78
- distance_to_high_60_pct: -6.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260601,348,359.5,342,356.5,1047654,378.92,-5.92,379.77,420.88,0.58
20260602,356.5,362,348,350,730473,376.51,-7.04,376.9,418.68,0.4
20260603,358,358,349,354,532240,374.63,-5.51,374.12,416.49,0.29
20260604,355.5,372.5,352.5,363,1310251,373.66,-2.85,371.57,415,0.71
20260605,364.5,377,360.5,371.5,1321960,373.48,-0.53,369.2,413.52,0.73
20260608,363.5,393.5,362.5,391,3431781,374.94,4.28,368.32,412.15,1.79
20260609,391,404.5,384,390,2666248,376.2,3.67,367.62,410.95,1.4
20260610,393,413,393,398,3305702,378.01,5.29,367.38,409.98,1.66
20260611,404,404,378.5,380.5,1662956,378.22,0.6,368.25,408.37,0.84
20260612,384,391,383,390.5,706145,379.25,2.97,370.12,406.85,0.39
20260615,397,416.5,394.5,410,1958717,381.81,7.38,371.23,405.08,1.12
20260616,407,412.5,398.5,405.5,1450773,383.78,5.66,372.9,403.79,0.87
20260617,405.5,421,405.5,412.5,1892782,386.18,6.82,374.35,402.61,1.15
20260618,417,425.5,413,422.5,1287852,389.2,8.56,376.27,402.09,0.79
20260622,425,439,414,423,1500221,392.02,7.9,378.45,401.54,0.93
20260623,428,449,427.5,439.5,2375348,395.98,10.99,382.1,401.18,1.45
20260624,443.5,448,437,443.5,1237489,399.94,10.89,386.5,400.99,0.76
20260625,445,445,418.5,419.5,1804544,401.57,4.47,390.15,400.4,1.1
20260626,424.5,426,409.5,412,842928,402.44,2.38,393.95,399.78,0.52
20260629,419,453,419,437.5,3026054,405.36,7.93,398.52,399.76,1.78
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 55.81
- over_600_ratio: 51
- over_800_ratio: 46.1
- over_1000_ratio: 45.45
- over_400_change_1w: 0.12
- over_800_change_1w: -0.58
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.45,,46.36,,45.08,,0,False,False
20260508,55.45,0,46.33,-0.03,45.05,-0.03,0,False,False
20260515,54.9,-0.55,45.62,-0.71,44.3,-0.75,0,False,False
20260522,55.01,0.11,46.24,0.62,44.92,0.62,1,True,True
20260529,54.88,-0.13,46.07,-0.17,44.75,-0.17,0,False,False
20260605,55.43,0.55,45.9,-0.17,44.58,-0.17,1,False,False
20260612,55.33,-0.1,46.62,0.72,45.32,0.74,2,False,True
20260618,55.69,0.36,46.68,0.06,45.39,0.07,3,False,True
20260626,55.81,0.12,46.1,-0.58,45.45,0.06,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260629 | 6472 | 保瑞 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_strong_inflow | stale_signal | 1.事實發生日:115/06/18 2.公開發行公司及其子公司資金貸與他人之餘額達該公開發行公司最近期財務報表 淨值百分之二十以上者: (1)接受資金貸與之公司名稱:Bora Pharmaceuticals USA Inc. (2)與資金貸與他人公司之關係: 本公司100%直接持股之子公司(由子公司Bora Global Ltd.貸與) (3)資金貸與之限額(仟元):3,897,602 (4)迄事實發生日為止資金貸與餘額(仟元):2,573,770 (5)迄事實發生日為止資金貸與原因: 充實收購馬里蘭州CDMO營運資產所需之營運資金。 (1)接受資金貸與之公司名稱:Bora Pharmaceuticals Inc. (2)與資金貸與他人公司之關係: 為本公司100%間接持股之子公司(由子公司Bora Pharmaceuticals USA Inc.貸與) (3)資金貸與之限額(仟元):26,821,545 (4)迄事實發生日為止資金貸與餘額(仟元):789,500 (5)迄事實發生日為止資金貸與原因: 充實Bora Pharmaceuticals Inc.拓展CDMO業務所需之營運資金。 (1)接受資金貸與之公司名稱:Upsher-Smith Laboratories, LLC (2)與資金貸與他人公司之關係: 為本公司100%間接持股之子公司(由子公司TWi Pharmaceuticals USA, Inc.貸與) (3)資金貸與之限額(仟元):26,821,545 (4)迄事實發生日為止資金貸與餘額(仟元):167,374 (5)迄事實發生日為止資金貸與原因: 充實營運資金及償還借款 (1)接受資金貸與之公司名稱:Upsher-Smith Laboratories, LLC (2)與資金貸與他人公司之關係: 為本公司100%間接持股之子公司(由子公司TWi Pharmaceuticals USA, Inc.貸與) (3)資金貸與之限額(仟元):2,438,660 (4)迄事實發生日為止資金貸與餘額(仟元):1,175,608 (5)迄事實發生日為止資金貸與原因: 充實營運資金以及逾期應收帳款轉列其他應收款。 (1)接受資金貸與之公司名稱:Bora Pharmaceuticals Injectables Inc. (2)與資金貸與他人公司之關係: 為本公司100%間接持股之子公司(由子公司Bora Pharmaceuticals USA Inc.貸與) (3)資金貸與之限額(仟元):26,821,545 (4)迄事實發生日為止資金貸與餘額(仟元):236,850 (5)迄事實發生日為止資金貸與原因: 充實營運資金及償還借款。 3.迄事實發生日為止，資金貸與餘額(仟元): 4,943,102 4.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 33.93 5.公司貸與他人資金之來源: 子公司本身 6.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260629 | 6472 | 保瑞 | 1 | 1 | 2 | 5 | 5 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260629 | 6472 | 保瑞 | 72 | 0 | 15763200.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
