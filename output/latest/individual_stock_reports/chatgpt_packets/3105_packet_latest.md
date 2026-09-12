# INDIVIDUAL STOCK CHATGPT PACKET - 3105 穩懋

## Metadata
- generated_at: 2026-09-12 15:43:11 Asia/Taipei
- stock_id: 3105
- stock_name: 穩懋
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 218
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3105_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3105_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3105_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3105_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3105_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3105_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3105_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3105_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3105_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3105_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3105_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3105_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3105.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3105.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3105.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3105.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3105_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3105_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3105_latest.md?ref=main

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
- date: 20260911
- open: 449.5
- high: 450
- low: 435
- close: 437.5
- volume: 14114000
- ma5: 451
- ema23_primary: 425.37
- distance_to_ema23_pct: 2.85
- ma20: 423.57
- ma60: 399.53
- ma120: 440.58
- return_5d: -2.67
- return_20d: 15.74
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: 3.29
- distance_to_high_60_pct: -23.65

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,391,404.5,388.5,398,24907000,371.66,7.09,351.62,427,1.1
20260818,400,406,373.5,374.5,28231000,371.9,0.7,353.38,424.39,1.21
20260819,353.5,374,351,363.5,17582000,371.2,-2.07,353.6,421.4,0.75
20260820,370,379,359.5,379,15615000,371.85,1.92,354.32,418.35,0.67
20260821,377,385.5,365.5,373,21808000,371.94,0.28,355.9,415.23,0.94
20260824,370.5,372.5,355,355,11814000,370.53,-4.19,355.9,412.35,0.54
20260825,350.5,381.5,349.5,379,16227000,371.24,2.09,358.7,409.88,0.75
20260826,378,405,374,405,31905000,374.05,8.27,364.4,407.8,1.46
20260827,413,445.5,412,445.5,36119000,380,17.24,373.27,406.57,1.61
20260828,449.5,461.5,434.5,439,48392000,384.92,14.05,380.5,405.31,2.01
20260831,434.5,471,425,447.5,50920000,390.14,14.7,387.32,404.64,1.98
20260901,448.5,492,444,492,55247000,398.62,23.42,394.82,404.78,2.01
20260902,484,492,468,469.5,41055000,404.53,16.06,399.5,405.08,1.39
20260903,478,490,440,446.5,40305000,408.03,9.43,402.73,404.25,1.37
20260904,465,465,438.5,449.5,23782000,411.48,9.24,406.9,403.77,0.81
20260907,453.5,463,446.5,450.5,19322000,414.74,8.62,410.15,403.26,0.66
20260908,457,458,440,441.5,17063000,416.97,5.88,413.68,402.2,0.58
20260909,462,478,457.5,464,35781000,420.89,10.24,416.88,401.42,1.21
20260910,462.5,465,452,461.5,14923000,424.27,8.78,420.6,400.89,0.53
20260911,449.5,450,435,437.5,14114000,425.37,2.85,423.57,399.53,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 52.91
- over_600_ratio: 50.03
- over_800_ratio: 48.12
- over_1000_ratio: 47.25
- over_400_change_1w: 0.13
- over_800_change_1w: 0.29
- over_1000_change_1w: 0.71
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,54.25,-1.44,50.08,-0.73,48.13,0.03,3,False,True
20260703,52.25,-2,48.61,-1.47,46.89,-1.24,0,False,False
20260709,51.78,-0.47,47.75,-0.86,46.67,-0.22,0,False,False
20260717,51.85,0.07,48.03,0.28,46.93,0.26,1,True,True
20260724,52.16,0.31,48.16,0.13,46.22,-0.71,2,False,True
20260731,51.14,-1.02,47.73,-0.43,46.22,0,0,False,False
20260807,51.58,0.44,47.9,0.17,46.34,0.12,1,True,True
20260814,50.45,-1.13,46.17,-1.73,44.4,-1.94,0,False,False
20260821,49.41,-1.04,44.63,-1.54,43.4,-1,0,False,False
20260828,53.51,4.1,48.3,3.67,47.25,3.85,1,True,True
20260904,52.78,-0.73,47.83,-0.47,46.54,-0.71,2,False,False
20260911,52.91,0.13,48.12,0.29,47.25,0.71,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 3105 | 穩懋 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會決議或公司決定日期:115/09/10 2.發行股數:不適用 3.每股面額:不適用 4.發行總金額:美金7,672,000元 5.發行價格:不適用 6.員工認股股數:不適用 7.原股東認購比率:100% 8.公開銷售方式及股數:不適用 9.畸零股及逾期未認購股份之處理方式:不適用 10.本次發行新股之權利義務:不適用 11.本次增資資金用途:充實營運資金暨償還借款 12.現金增資認股基準日:115/10/31 13.最後過戶日:不適用 14.停止過戶起始日期:不適用 15.停止過戶截止日期:不適用 16.股款繳納期間:不適用 17.與代收及專戶存儲價款行庫訂約日期:不適用 18.委託代收款項機構:不適用 19.委託存儲款項機構:不適用 20.其他應敘明事項: 本次增資將由其母公司Chainwin Biotech and Agrotech (Cayman Islands) Co., Ltd. 全數認購，其資金來源係由Chainwin Biotech and Agrotech (Cayman Islands) Co., Ltd.洽特定人所募得之股款。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 3105 | 穩懋 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  |  | stale_signal | 1.董事會決議或公司決定日期:115/09/10 2.發行股數:不適用 3.每股面額:不適用 4.發行總金額:美金7,672,000元 5.發行價格:不適用 6.員工認股股數:不適用 7.原股東認購比率:100% 8.公開銷售方式及股數:不適用 9.畸零股及逾期未認購股份之處理方式:不適用 10.本次發行新股之權利義務:不適用 11.本次增資資金用途:充實營運資金暨償還借款 12.現金增資認股基準日:115/10/31 13.最後過戶日:不適用 14.停止過戶起始日期:不適用 15.停止過戶截止日期:不適用 16.股款繳納期間:不適用 17.與代收及專戶存儲價款行庫訂約日期:不適用 18.委託代收款項機構:不適用 19.委託存儲款項機構:不適用 20.其他應敘明事項: 本次增資將由其母公司Chainwin Biotech and Agrotech (Cayman Islands) Co., Ltd. 全數認購，其資金來源係由Chainwin Biotech and Agrotech (Cayman Islands) Co., Ltd.洽特定人所募得之股款。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 3105 | 穩懋 | 1 | 1 | 2 | 4 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
