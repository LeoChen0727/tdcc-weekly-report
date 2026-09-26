# INDIVIDUAL STOCK CHATGPT PACKET - 4416 三圓

## Metadata
- generated_at: 2026-09-26 15:52:16 Asia/Taipei
- stock_id: 4416
- stock_name: 三圓
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 255
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4416_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4416_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4416.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4416.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4416.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4416.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4416_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4416_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4416_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260924
- open: 14
- high: 14.1
- low: 13.4
- close: 13.7
- volume: 1316000
- ma5: 13.36
- ema23_primary: 12.44
- distance_to_ema23_pct: 10.16
- ma20: 12.35
- ma60: 11.61
- ma120: 11.83
- return_5d: 23.98
- return_20d: -5.52
- volume_ratio: 0.83
- distance_to_ma20_pct_auxiliary: 10.93
- distance_to_high_60_pct: -15.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,14.5,14.6,14,14.05,1075000,12.46,12.76,12.03,11.19,0.87
20260831,12.65,13.2,12.65,12.7,2411000,12.48,1.76,12.14,11.21,1.78
20260901,12.7,12.75,12.3,12.45,1131000,12.48,-0.22,12.26,11.23,0.81
20260902,12.5,12.8,12.4,12.65,575000,12.49,1.27,12.37,11.25,0.4
20260903,12.6,12.85,12.4,12.4,604000,12.48,-0.67,12.46,11.28,0.42
20260904,12.5,12.9,12.45,12.75,506000,12.51,1.95,12.57,11.32,0.35
20260907,12.75,13.15,12.35,12.35,666000,12.49,-1.15,12.66,11.35,0.45
20260908,12.35,12.35,12.05,12.05,625000,12.46,-3.26,12.74,11.37,0.41
20260909,12.05,12.1,11.8,11.9,493000,12.41,-4.11,12.81,11.39,0.32
20260910,12.05,12.05,11.3,11.3,988000,12.32,-8.26,12.86,11.41,0.63
20260911,11.3,11.3,11,11,771000,12.21,-9.89,12.87,11.44,0.51
20260914,10.95,10.95,10.25,10.75,1596000,12.09,-11.06,12.85,11.45,1.04
20260915,10.7,11.8,10.7,11.6,2123000,12.05,-3.7,12.82,11.47,1.38
20260916,11.4,11.5,11.05,11.2,1133000,11.98,-6.47,12.76,11.49,0.79
20260917,11.25,11.3,10.8,11.05,1517000,11.9,-7.13,12.69,11.49,1.05
20260918,11.25,12.15,11.15,12.15,4528000,11.92,1.94,12.61,11.49,2.88
20260921,12.2,13.35,12.2,13.35,2293000,12.04,10.9,12.52,11.5,1.42
20260922,14.15,14.35,13.2,13.5,5216000,12.16,11.02,12.43,11.53,3.18
20260923,13.5,14.5,13.05,14.1,2095000,12.32,14.43,12.39,11.57,1.31
20260924,14,14.1,13.4,13.7,1316000,12.44,10.16,12.35,11.61,0.83
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 65.85
- over_600_ratio: 57.16
- over_800_ratio: 52.51
- over_1000_ratio: 49.85
- over_400_change_1w: -1.61
- over_800_change_1w: -3.75
- over_1000_change_1w: -3.75
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,75.01,-0.19,64.87,-0.05,62.2,-0.05,0,False,False
20260717,73.14,-1.87,64.22,-0.65,61.55,-0.65,0,False,False
20260724,73.53,0.39,64.02,-0.2,61.35,-0.2,1,False,False
20260731,72.73,-0.8,63.75,-0.27,61.08,-0.27,0,False,False
20260807,72.63,-0.1,63.61,-0.14,60.94,-0.14,0,False,False
20260814,72.53,-0.1,63.45,-0.16,60.78,-0.16,0,False,False
20260821,70.89,-1.64,61.25,-2.2,58.59,-2.19,0,False,False
20260828,70.79,-0.1,61.43,0.18,57.44,-1.15,1,False,True
20260904,70.32,-0.47,60.13,-1.3,57.47,0.03,2,False,True
20260911,70.48,0.16,59.52,-0.61,56.86,-0.61,3,False,False
20260918,67.46,-3.02,56.26,-3.26,53.6,-3.26,0,False,False
20260924,65.85,-1.61,52.51,-3.75,49.85,-3.75,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4416 | 三圓 | revenue_pullback | 營收成長股價回檔 | 55.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | continued_overheated | 1.關係人或主要債務人或其連帶保證人名稱:山圓建設股份有限公司 2.事實發生日:115/09/23 3.發生緣由:本公司於115/09/23接獲通知，山圓建設(股)公司於115/09/23因存款不足 發生退票資訊如下:合作金庫銀行之支票4張，金額合計:新台幣400,000,000元。 4.債權種類或背書保證金額及其所占資產比例:不適用 5.債權有無保全措施:不適用 6.對公司財務、業務之影響及預計可能損失:本公司第二季財報帳列 (1)其他應收款-其他關係人-山圓共計新台幣373,579仟元，提列減損新台幣373,579仟元 (2)資金融通-其他關係人-山圓共計新台幣87,795仟元，提列減損新台幣87,795仟元 7.因應措施:與持票人協商清償註記。 8.其他應敘明事項: (1)截至本日共有75張支票尚未清償註記，金額共計新台幣1,600,817,940。 (2)因期限內超過3張未清償註記，目前為拒絕往來戶。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4416 | 三圓 | 7 | 1 | 5 | 7 | 10 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
