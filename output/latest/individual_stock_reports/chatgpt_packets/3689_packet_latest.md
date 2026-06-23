# INDIVIDUAL STOCK CHATGPT PACKET - 3689 湧德

## Metadata
- generated_at: 2026-06-23 22:23:42 Asia/Taipei
- stock_id: 3689
- stock_name: 湧德
- packet_status: standard_180d_window_packet
- latest_price_date: 20260622
- price_rows: 153
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3689_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3689_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3689.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3689.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3689.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3689.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3689_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3689_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3689_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- decision_score_high
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
- date: 20260622
- open: 122
- high: 122
- low: 120
- close: 120.5
- volume: 1441000
- ma5: 119.4
- ema23_primary: 124.21
- distance_to_ema23_pct: -2.99
- ma20: 126.95
- ma60: 126.69
- ma120: 120.25
- return_5d: 3.88
- return_20d: -2.43
- volume_ratio: 1.14
- distance_to_ma20_pct_auxiliary: -5.08
- distance_to_high_60_pct: -17.47

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260525,125,126.5,123,125,125000,124.83,0.14,126.78,121.3,0.03
20260526,127,127.5,123.5,124.5,125000,124.8,-0.24,126.42,121.41,0.04
20260527,126.5,132.5,123.5,130.5,129000,125.27,4.17,126.35,121.61,0.04
20260528,134,139.5,130.5,132,135000,125.83,4.9,126.38,121.89,0.04
20260529,136.5,138.5,133.5,138,136000,126.85,8.79,126.58,122.32,0.04
20260601,139,144,136,137.5,140000,127.74,7.64,126.62,122.88,0.05
20260602,138,138.5,133,136,136,128.42,5.9,126.47,123.36,0
20260603,138.5,145,137.5,142,142000,129.56,9.61,126.47,123.96,0.07
20260604,141,144.5,138,141,141000,130.51,8.04,127.12,124.67,0.1
20260605,139,142,133.5,141.5,138000,131.43,7.67,127.9,125.33,0.12
20260608,127.5,127.5,127.5,127.5,1700000,131.1,-2.74,128.05,125.71,1.68
20260609,127.5,127.5,119,122,6383000,130.34,-6.4,127.95,126.05,5.2
20260610,120,125.5,115,115,4412000,129.06,-10.9,127.6,126.26,3.27
20260611,115.5,116.5,110,113.5,2821000,127.76,-11.16,127.12,126.42,2.06
20260612,117,118.5,116,116,1612000,126.78,-8.51,126.97,126.53,1.25
20260615,118,121.5,118,119.5,1903000,126.18,-5.29,127.08,126.5,1.48
20260616,121.5,122,117,117.5,1312000,125.45,-6.34,127.1,126.39,1.05
20260617,116,118.5,115.5,118.5,853000,124.87,-5.1,127.1,126.42,0.71
20260618,119,122,119,121,1545000,124.55,-2.85,127.1,126.54,1.29
20260622,122,122,120,120.5,1441000,124.21,-2.99,126.95,126.69,1.14
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 27.45
- over_600_ratio: 20.92
- over_800_ratio: 18.61
- over_1000_ratio: 15.51
- over_400_change_1w: -0.65
- over_800_change_1w: -1.09
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,32.37,,22.89,,15.94,,0,False,False
20260508,25.31,-7.06,16.67,-6.22,12.56,-3.38,0,False,False
20260515,24.7,-0.61,17.58,0.91,12.56,0,1,False,True
20260522,23.12,-1.58,16.67,-0.91,12.56,0,0,False,False
20260529,29.33,6.21,20.24,3.57,17.13,4.57,1,True,True
20260605,32.95,3.62,23.41,3.17,19.38,2.25,2,True,True
20260612,28.1,-4.85,19.7,-3.71,15.66,-3.72,0,False,False
20260618,27.45,-0.65,18.61,-1.09,15.51,-0.15,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260622 | 3689 | 湧德 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/18 2.公開發行公司及其子公司資金貸與他人之餘額達該公開發行公司最近期財務報表 淨值百分之二十以上者: (1)接受資金貸與之公司名稱:U.D.ELECTRONIC VIETNAM COMPANY (2)與資金貸與他人公司之關係: 湧德電子股份有限公司資金貸與湧德電子股份有限公司持股100% 直接投資之越南湧德有限公司。 (3)資金貸與之限額(仟元):1,885,103 (4)迄事實發生日為止資金貸與餘額(仟元):1,091,155 (5)迄事實發生日為止資金貸與原因: 營運週轉。 (1)接受資金貸與之公司名稱:東莞德洋精密橡塑有限公司 (2)與資金貸與他人公司之關係: 湧德電子股份有限公司持股51%間接投資之Morning Paragon Limited資金貸與 湧德間接持股51%之東莞德洋精密橡塑有限公司。 (3)資金貸與之限額(仟元):28,114 (4)迄事實發生日為止資金貸與餘額(仟元):27,135 (5)迄事實發生日為止資金貸與原因: 營運週轉。 (1)接受資金貸與之公司名稱:東莞德洋精密橡塑有限公司 (2)與資金貸與他人公司之關係: 湧德電子股份有限公司持股100%間接投資之中江湧德電子有限公司資金貸與 湧德間接持股51%之東莞德洋精密橡塑有限公司。 (3)資金貸與之限額(仟元):1,122,400 (4)迄事實發生日為止資金貸與餘額(仟元):193,163 (5)迄事實發生日為止資金貸與原因: 營運週轉。 (1)接受資金貸與之公司名稱:中江湧德電子有限公司 (2)與資金貸與他人公司之關係: 湧德電子股份有限公司持股100%間接投資之聯網電子有限公司資金貸與 湧德間接持股100%之中江湧德電子有限公司。 (3)資金貸與之限額(仟元):36,682 (4)迄事實發生日為止資金貸與餘額(仟元):27,595 (5)迄事實發生日為止資金貸與原因: 營運週轉。 (1)接受資金貸與之公司名稱:浙江榆陽電子股份有限公司 (2)與資金貸與他人公司之關係: 湧德電子股份有限公司持股91.09%間接投資之浙江榆陽電子股份有限公司 資金貸與湧德間接持股91.09%之杭州栖谷科技有限公司。 (3)資金貸與之限額(仟元):483,419 (4)迄事實發生日為止資金貸與餘額(仟元):5,519 (5)迄事實發生日為止資金貸與原因: 營運週轉。 3.迄事實發生日為止，資金貸與餘額(仟元): 1,344,566 4.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 28.53 5.公司貸與他人資金之來源: 子公司本身、母公司 6.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260622 | 3689 | 湧德 | 1 | 1 | 1 | 2 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
