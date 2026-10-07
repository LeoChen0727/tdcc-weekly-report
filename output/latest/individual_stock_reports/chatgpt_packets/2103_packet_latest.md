# INDIVIDUAL STOCK CHATGPT PACKET - 2103 台橡

## Metadata
- generated_at: 2026-10-07 22:17:12 Asia/Taipei
- stock_id: 2103
- stock_name: 台橡
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 366
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
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
- date: 20261002
- open: 28.1
- high: 29
- low: 27.9
- close: 28.15
- volume: 4869851
- ma5: 27.89
- ema23_primary: 27.34
- distance_to_ema23_pct: 2.98
- ma20: 27.19
- ma60: 25.88
- ma120: 23.22
- return_5d: 0.9
- return_20d: -0.53
- volume_ratio: 1.14
- distance_to_ma20_pct_auxiliary: 3.53
- distance_to_high_60_pct: -4.41

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,28.2,28.9,27.9,27.95,4443020,27.01,3.47,27.82,24.19,0.5
20260904,28.2,28.3,27.7,28.25,3274701,27.12,4.18,27.98,24.31,0.37
20260907,28.45,28.45,27.2,27.4,6933841,27.14,0.96,27.97,24.39,0.86
20260908,27.25,27.25,25.3,25.75,14934234,27.02,-4.71,27.83,24.45,2.18
20260909,25.8,26.6,25.7,26.5,4099892,26.98,-1.78,27.79,24.52,0.66
20260910,26.55,26.55,25.7,25.85,3930753,26.89,-3.85,27.67,24.59,0.67
20260911,25.5,25.95,25.3,25.75,2539776,26.79,-3.89,27.62,24.66,0.46
20260914,25.7,25.75,25.15,25.45,2689775,26.68,-4.61,27.52,24.73,0.5
20260915,25.5,25.8,25.35,25.75,1765093,26.6,-3.2,27.41,24.8,0.34
20260916,25.75,27.15,25.75,26.85,6778855,26.62,0.85,27.39,24.9,1.31
20260917,27,28.45,26.75,28.2,7673485,26.75,5.4,27.41,25,1.45
20260918,28.35,28.35,27.3,27.6,4600637,26.82,2.89,27.37,25.11,0.9
20260921,27.9,27.95,27.4,27.8,1778319,26.91,3.32,27.34,25.23,0.36
20260922,27.95,27.95,27.2,27.35,2248619,26.94,1.51,27.3,25.34,0.46
20260923,27.6,28.3,27.55,27.9,4459016,27.02,3.25,27.29,25.46,0.9
20260924,27.9,27.9,27.4,27.8,1545422,27.09,2.63,27.29,25.58,0.33
20260929,27.8,28,27.4,27.4,2596683,27.11,1.06,27.25,25.68,0.57
20260930,27.5,28.2,27.5,28.15,2618484,27.2,3.49,27.24,25.76,0.57
20261001,28.1,28.2,27.7,27.95,1423826,27.26,2.52,27.2,25.82,0.33
20261002,28.1,29,27.9,28.15,4869851,27.34,2.98,27.19,25.88,1.14
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 59.94
- over_600_ratio: 57.88
- over_800_ratio: 56.47
- over_1000_ratio: 54.94
- over_400_change_1w: 0.04
- over_800_change_1w: 0.18
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,56.6,0.06,53.38,0.09,51.9,0.1,7,False,True
20260724,56.49,-0.11,53.01,-0.37,51.61,-0.29,0,False,False
20260731,56.48,-0.01,53.22,0.21,51.72,0.11,1,False,True
20260807,56.56,0.08,53.1,-0.12,51.72,0,2,False,False
20260814,58.97,2.41,55.42,2.32,54.47,2.75,3,True,True
20260821,58.62,-0.35,55.27,-0.15,54.09,-0.38,0,False,False
20260828,58.95,0.33,55.36,0.09,54.16,0.07,1,True,True
20260904,59.11,0.16,55.5,0.14,54.44,0.28,2,True,True
20260911,58.77,-0.34,55.54,0.04,54.23,-0.21,3,False,True
20260918,59.61,0.84,56.09,0.55,54.78,0.55,4,True,True
20260924,59.9,0.29,56.29,0.2,54.98,0.2,5,True,True
20261002,59.94,0.04,56.47,0.18,54.94,-0.04,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2103 | 台橡 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/07/17 2.接受資金貸與之: (1)公司名稱:TSRC Specialty Materials LLC (2)與資金貸與他人公司之關係: Polybus Corporation Pte Ltd與TSRC Specialty Materials LLC, 均為 台橡股份有限公司100%間接持股之子公司 (3)資金貸與之限額(仟元):7,328,042 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):643,440 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):643,440 (8)本次新增資金貸與之原因: 因應TSRC Specialty Materials LLC營運資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無擔保品 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):0 (2)累積盈虧金額(仟元):165,741 5.計息方式: Term SOFR+1.1% 6.還款之: (1)條件: 依合約規範 (2)日期: 自首次撥款日起算二年 7.迄事實發生日為止，資金貸與餘額(仟元): 1,970,693 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 9.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: Polybus Corporation Pte Ltd原於2024年10月25日與 TSRC Specialty Materials LLC簽訂美金1,000萬元借款協議, 由於 不再使用借款額度,經雙方合意提前終止協議, 並經雙方董事會通過後生效；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2103 | 台橡 | 22 | 1 | 5 | 10 | 20 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 20 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2103 | 台橡 | 23 | 0 | 1288710.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
