# INDIVIDUAL STOCK CHATGPT PACKET - 2103 台橡

## Metadata
- generated_at: 2026-09-06 22:16:11 Asia/Taipei
- stock_id: 2103
- stock_name: 台橡
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
- date: 20260904
- open: 28.2
- high: 28.3
- low: 27.7
- close: 28.25
- volume: 3274701
- ma5: 28.34
- ema23_primary: 27.12
- distance_to_ema23_pct: 4.18
- ma20: 27.98
- ma60: 24.31
- ma120: 22.14
- return_5d: 0.18
- return_20d: 13
- volume_ratio: 0.37
- distance_to_ma20_pct_auxiliary: 0.97
- distance_to_high_60_pct: -4.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,27.3,27.5,26.8,27.5,24706261,22.95,19.81,23.16,21.88,3.24
20260811,27.8,28.95,27.5,28.65,38321753,23.43,22.29,23.34,22.01,4.38
20260812,28.25,28.35,27.25,27.35,16248653,23.76,15.13,23.43,22.12,1.81
20260813,27.55,28.2,26.9,28.1,11391365,24.12,16.51,23.6,22.25,1.33
20260814,28.15,28.2,26.8,26.85,9188272,24.35,10.29,23.77,22.36,1.07
20260817,26.8,27.95,26.8,27.5,5406064,24.61,11.75,23.99,22.48,0.63
20260818,27.5,28,27.25,27.85,5082989,24.88,11.95,24.2,22.61,0.59
20260819,27.5,27.75,26.8,27.25,8185141,25.08,8.67,24.36,22.74,0.93
20260820,27.55,28.2,27.3,27.85,5727413,25.31,10.05,24.56,22.89,0.65
20260821,27.9,28.8,27.6,28.4,7697215,25.56,11.09,24.81,23.05,0.86
20260824,28.6,28.8,27.65,28.3,6462701,25.79,9.72,25.12,23.2,0.72
20260825,28.15,28.25,27.8,28.1,2887777,25.98,8.14,25.46,23.35,0.33
20260826,28,28.3,27.85,28.2,2989053,26.17,7.76,25.84,23.5,0.35
20260827,28.25,28.9,27.7,27.75,7270481,26.3,5.51,26.2,23.62,0.84
20260828,27.9,28.45,27.85,28.2,3820263,26.46,6.58,26.55,23.73,0.45
20260831,28.3,28.55,28.05,28.4,2912222,26.62,6.68,26.91,23.83,0.34
20260901,28.35,29.45,28.2,28.8,7394990,26.8,7.45,27.26,23.95,0.84
20260902,28.65,29.05,27.95,28.3,5051843,26.93,5.1,27.55,24.07,0.57
20260903,28.2,28.9,27.9,27.95,4443020,27.01,3.47,27.82,24.19,0.5
20260904,28.2,28.3,27.7,28.25,3274701,27.12,4.18,27.98,24.31,0.37
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 59.11
- over_600_ratio: 56.74
- over_800_ratio: 55.5
- over_1000_ratio: 54.44
- over_400_change_1w: 0.16
- over_800_change_1w: 0.14
- over_1000_change_1w: 0.28
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,54.68,0.31,51.22,0.65,49.8,0.76,3,True,True
20260626,55.11,0.43,51.45,0.23,50.14,0.34,4,True,True
20260703,55.1,-0.01,51.56,0.11,50.17,0.03,5,False,True
20260709,56.54,1.44,53.29,1.73,51.8,1.63,6,True,True
20260717,56.6,0.06,53.38,0.09,51.9,0.1,7,False,True
20260724,56.49,-0.11,53.01,-0.37,51.61,-0.29,0,False,False
20260731,56.48,-0.01,53.22,0.21,51.72,0.11,1,False,True
20260807,56.56,0.08,53.1,-0.12,51.72,0,2,False,False
20260814,58.97,2.41,55.42,2.32,54.47,2.75,3,True,True
20260821,58.62,-0.35,55.27,-0.15,54.09,-0.38,0,False,False
20260828,58.95,0.33,55.36,0.09,54.16,0.07,1,True,True
20260904,59.11,0.16,55.5,0.14,54.44,0.28,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2103 | 台橡 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/07/17 2.接受資金貸與之: (1)公司名稱:TSRC Specialty Materials LLC (2)與資金貸與他人公司之關係: Polybus Corporation Pte Ltd與TSRC Specialty Materials LLC, 均為 台橡股份有限公司100%間接持股之子公司 (3)資金貸與之限額(仟元):7,328,042 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):643,440 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):643,440 (8)本次新增資金貸與之原因: 因應TSRC Specialty Materials LLC營運資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無擔保品 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):0 (2)累積盈虧金額(仟元):165,741 5.計息方式: Term SOFR+1.1% 6.還款之: (1)條件: 依合約規範 (2)日期: 自首次撥款日起算二年 7.迄事實發生日為止，資金貸與餘額(仟元): 1,970,693 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 9.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: Polybus Corporation Pte Ltd原於2024年10月25日與 TSRC Specialty Materials LLC簽訂美金1,000萬元借款協議, 由於 不再使用借款額度,經雙方合意提前終止協議, 並經雙方董事會通過後生效；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 2103 | 台橡 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/07/17 2.接受資金貸與之: (1)公司名稱:TSRC Specialty Materials LLC (2)與資金貸與他人公司之關係: Polybus Corporation Pte Ltd與TSRC Specialty Materials LLC, 均為 台橡股份有限公司100%間接持股之子公司 (3)資金貸與之限額(仟元):7,328,042 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):643,440 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):643,440 (8)本次新增資金貸與之原因: 因應TSRC Specialty Materials LLC營運資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無擔保品 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):0 (2)累積盈虧金額(仟元):165,741 5.計息方式: Term SOFR+1.1% 6.還款之: (1)條件: 依合約規範 (2)日期: 自首次撥款日起算二年 7.迄事實發生日為止，資金貸與餘額(仟元): 1,970,693 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 9.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: Polybus Corporation Pte Ltd原於2024年10月25日與 TSRC Specialty Materials LLC簽訂美金1,000萬元借款協議, 由於 不再使用借款額度,經雙方合意提前終止協議, 並經雙方董事會通過後生效；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2103 | 台橡 | 6 | 6 | 5 | 8 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2103 | 台橡 | 21 | 0 | 1080140.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
