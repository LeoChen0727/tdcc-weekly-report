# INDIVIDUAL STOCK CHATGPT PACKET - 2103 台橡

## Metadata
- generated_at: 2026-07-20 22:26:42 Asia/Taipei
- stock_id: 2103
- stock_name: 台橡
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2103_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2103_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2103_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2103_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2103_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2103_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2103_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2103_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2103_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2103_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2103_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2103_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2103.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2103.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2103.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2103.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2103_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2103_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2103_latest.md?ref=main

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
- date: 20260717
- open: 24.1
- high: 24.5
- low: 23.35
- close: 23.5
- volume: 8033829
- ma5: 24.39
- ema23_primary: 22.84
- distance_to_ema23_pct: 2.87
- ma20: 22.61
- ma60: 21.14
- ma120: 19.71
- return_5d: 1.95
- return_20d: 10.85
- volume_ratio: 0.94
- distance_to_ma20_pct_auxiliary: 3.96
- distance_to_high_60_pct: -14.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,21.2,22.05,21.2,21.4,4944708,21.02,1.83,20.76,20.09,0.84
20260622,21.4,21.8,21.2,21.4,3468206,21.05,1.67,20.84,20.12,0.6
20260623,21.65,21.65,21.05,21.15,3301457,21.06,0.44,20.92,20.15,0.58
20260624,20.85,22.1,20.35,21.95,6880029,21.13,3.88,21.05,20.18,1.17
20260625,22.05,22.1,21.4,21.45,4479656,21.16,1.38,21.19,20.22,0.78
20260626,21.75,21.75,20.1,20.25,6076399,21.08,-3.95,21.25,20.22,1.03
20260629,20.25,20.75,20.1,20.65,2451973,21.05,-1.88,21.33,20.25,0.42
20260630,20.65,20.9,20.4,20.7,1803886,21.02,-1.51,21.39,20.27,0.31
20260701,20.9,21.05,20.55,20.6,2112008,20.98,-1.82,21.41,20.3,0.38
20260702,20.4,21.4,20.35,21.4,3099843,21.02,1.82,21.4,20.32,0.6
20260703,21.35,23.5,21.35,23.5,20839602,21.22,10.72,21.46,20.4,3.67
20260706,25.5,25.85,24.05,24.2,29304824,21.47,12.71,21.59,20.48,4.32
20260707,24.3,24.95,24.2,24.65,9764817,21.74,13.4,21.76,20.56,1.4
20260708,24.7,24.85,23.45,23.8,6841219,21.91,8.63,21.9,20.63,0.96
20260709,23.7,23.7,22.5,23.05,7574618,22,4.75,22,20.68,1.03
20260713,22.95,23.4,22.9,23.3,2983938,22.11,5.37,22.05,20.75,0.42
20260714,23.9,25.3,23.55,25,15820391,22.35,11.84,22.2,20.84,2.11
20260715,24,25.7,23.8,25.6,11954004,22.62,13.16,22.36,20.95,1.54
20260716,27.6,27.6,24.3,24.55,20009859,22.78,7.75,22.49,21.05,2.35
20260717,24.1,24.5,23.35,23.5,8033829,22.84,2.87,22.61,21.14,0.94
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 56.6
- over_600_ratio: 54.05
- over_800_ratio: 53.38
- over_1000_ratio: 51.9
- over_400_change_1w: 0.06
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.56,,48.97,,47.79,,0,False,False
20260508,52.6,0.04,48.99,0.02,47.89,0.1,1,False,True
20260515,53.72,1.12,50.45,1.46,48.61,0.72,2,True,True
20260522,53.16,-0.56,49.72,-0.73,48.3,-0.31,0,False,False
20260529,52.6,-0.56,49.05,-0.67,47.42,-0.88,0,False,False
20260605,54.1,1.5,50.51,1.46,48.98,1.56,1,True,True
20260612,54.37,0.27,50.57,0.06,49.04,0.06,2,True,True
20260618,54.68,0.31,51.22,0.65,49.8,0.76,3,True,True
20260626,55.11,0.43,51.45,0.23,50.14,0.34,4,True,True
20260703,55.1,-0.01,51.56,0.11,50.17,0.03,5,False,True
20260709,56.54,1.44,53.29,1.73,51.8,1.63,6,True,True
20260717,56.6,0.06,53.38,0.09,51.9,0.1,7,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2103 | 台橡 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/07/17 2.接受資金貸與之: (1)公司名稱:TSRC Specialty Materials LLC (2)與資金貸與他人公司之關係: Polybus Corporation Pte Ltd與TSRC Specialty Materials LLC, 均為 台橡股份有限公司100%間接持股之子公司 (3)資金貸與之限額(仟元):7,328,042 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):643,440 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):643,440 (8)本次新增資金貸與之原因: 因應TSRC Specialty Materials LLC營運資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無擔保品 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):0 (2)累積盈虧金額(仟元):165,741 5.計息方式: Term SOFR+1.1% 6.還款之: (1)條件: 依合約規範 (2)日期: 自首次撥款日起算二年 7.迄事實發生日為止，資金貸與餘額(仟元): 1,970,693 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 9.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: Polybus Corporation Pte Ltd原於2024年10月25日與 TSRC Specialty Materials LLC簽訂美金1,000萬元借款協議, 由於 不再使用借款額度,經雙方合意提前終止協議, 並經雙方董事會通過後生效；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2103 | 台橡 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/07/17 2.接受資金貸與之: (1)公司名稱:TSRC Specialty Materials LLC (2)與資金貸與他人公司之關係: Polybus Corporation Pte Ltd與TSRC Specialty Materials LLC, 均為 台橡股份有限公司100%間接持股之子公司 (3)資金貸與之限額(仟元):7,328,042 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):643,440 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):643,440 (8)本次新增資金貸與之原因: 因應TSRC Specialty Materials LLC營運資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無擔保品 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):0 (2)累積盈虧金額(仟元):165,741 5.計息方式: Term SOFR+1.1% 6.還款之: (1)條件: 依合約規範 (2)日期: 自首次撥款日起算二年 7.迄事實發生日為止，資金貸與餘額(仟元): 1,970,693 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 9.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: Polybus Corporation Pte Ltd原於2024年10月25日與 TSRC Specialty Materials LLC簽訂美金1,000萬元借款協議, 由於 不再使用借款額度,經雙方合意提前終止協議, 並經雙方董事會通過後生效；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2103 | 台橡 | 6 | 2 | 5 | 9 | 15 | repeated_but_no_breakout | 近 10 日上榜 9 次、近 20 日上榜 15 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2103 | 台橡 | 12 | 0 | 5624220.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
