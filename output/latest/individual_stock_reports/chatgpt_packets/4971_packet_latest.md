# INDIVIDUAL STOCK CHATGPT PACKET - 4971 IET-KY

## Metadata
- generated_at: 2026-09-20 22:17:22 Asia/Taipei
- stock_id: 4971
- stock_name: IET-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4971_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4971_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4971_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4971_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4971_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4971_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4971_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4971_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4971_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4971_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4971_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4971_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4971.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4971.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4971.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4971.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4971_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4971_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4971_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- open: 566
- high: 592
- low: 558
- close: 592
- volume: 2134000
- ma5: 554.8
- ema23_primary: 564.87
- distance_to_ema23_pct: 4.8
- ma20: 584.75
- ma60: 494.57
- ma120: 590.13
- return_5d: 7.64
- return_20d: 0.68
- volume_ratio: 0.81
- distance_to_ma20_pct_auxiliary: 1.24
- distance_to_high_60_pct: -18.46

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,575,581,530,530,3327000,491.92,7.74,468,499.86,1.58
20260825,520,554,502,554,525000,497.09,11.45,476.2,496.59,0.25
20260826,557,562,538,552,493000,501.67,10.03,486.25,492.64,0.24
20260827,552,570,531,567,681000,507.11,11.81,498.8,490.24,0.34
20260828,560,573,545,568,404000,512.19,10.9,509.82,487.77,0.2
20260831,555,600,555,600,794000,519.5,15.49,520.73,486.51,0.39
20260901,612,660,600,660,5343000,531.21,24.24,532.73,486.34,2.34
20260902,654,726,650,669,8383000,542.69,23.27,543.08,487.44,3.12
20260903,678,719,605,611,8356000,548.39,11.42,549.62,487.51,2.89
20260904,639,644,589,624,4905000,554.69,12.5,557.8,488.79,1.64
20260907,633,635,606,610,2012000,559.3,9.07,563.2,490.32,0.68
20260908,615,638,596,605,1885000,563.11,7.44,570.2,491.44,0.63
20260909,634,664,606,621,2392000,567.93,9.34,576.25,492.61,0.77
20260910,613,627,600,600,1612000,570.6,5.15,581.55,493.49,0.51
20260911,589,590,550,550,1562000,568.89,-3.32,585.05,493.89,0.49
20260914,531,559,531,531,1378000,565.73,-6.14,585.2,493.11,0.43
20260915,524,557,520,522,1399000,562.08,-7.13,583.5,492.29,0.47
20260916,530,574,530,574,2213000,563.08,1.94,585.8,492.86,0.77
20260917,604,606,555,555,2995000,562.4,-1.32,584.55,493.34,1.07
20260918,566,592,558,592,2134000,564.87,4.8,584.75,494.57,0.81
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 44.39
- over_600_ratio: 31.44
- over_800_ratio: 24.06
- over_1000_ratio: 22.03
- over_400_change_1w: 0.73
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,34.19,-0.26,11.59,-0.07,7.02,-0.02,0,False,False
20260709,34.04,-0.15,9.49,-2.1,7.02,0,0,False,False
20260717,47.05,13.01,24.14,14.65,22.05,15.03,1,True,True
20260724,46.7,-0.35,24.17,0.03,22.08,0.03,2,False,True
20260731,46.48,-0.22,26.4,2.23,24.31,2.23,3,False,True
20260807,45.42,-1.06,26.32,-0.08,22.12,-2.19,0,False,False
20260814,44.42,-1,24.18,-2.14,22.09,-0.03,0,False,False
20260821,46.27,1.85,24.06,-0.12,21.97,-0.12,1,False,False
20260828,44.24,-2.03,24.07,0.01,21.98,0.01,2,False,True
20260904,44.4,0.16,24.02,-0.05,21.98,0,3,False,False
20260911,43.66,-0.74,24.1,0.08,22.07,0.09,4,False,True
20260918,44.39,0.73,24.06,-0.04,22.03,-0.04,5,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 4971 | IET-KY | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/09/16 1.召開法人說明會之日期：115/09/16 2.召開法人說明會之時間：10 時 00 分 3.召開法人說明會之地點：線上連結 4.法人說明會擇要訊息：本公司受邀參加統一證舉辦法人座談會，會中就本公司已公開之資訊進行說明。 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 4971 | IET-KY | revenue_pullback | 營收成長股價回檔 | 69.0 |  |  |  |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/09/16 1.召開法人說明會之日期：115/09/16 2.召開法人說明會之時間：10 時 00 分 3.召開法人說明會之地點：線上連結 4.法人說明會擇要訊息：本公司受邀參加統一證舉辦法人座談會，會中就本公司已公開之資訊進行說明。 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 4971 | IET-KY | 3 | 3 | 4 | 5 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
