# INDIVIDUAL STOCK CHATGPT PACKET - 5388 中磊

## Metadata
- generated_at: 2026-09-19 22:17:00 Asia/Taipei
- stock_id: 5388
- stock_name: 中磊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5388_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5388_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5388_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5388_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5388_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5388_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5388_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5388_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5388_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5388_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5388_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5388_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5388.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5388.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5388.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5388.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5388_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5388_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5388_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- open: 74.6
- high: 74.6
- low: 73.2
- close: 73.6
- volume: 1902797
- ma5: 72.48
- ema23_primary: 75.5
- distance_to_ema23_pct: -2.52
- ma20: 74.8
- ma60: 80.98
- ma120: 81.82
- return_5d: 2.65
- return_20d: -5.15
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: -1.6
- distance_to_high_60_pct: -22.53

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,77.9,78.6,77.6,77.6,2131146,82.75,-6.22,83.89,84.5,0.38
20260825,78.3,78.3,76.5,77.1,3351309,82.28,-6.29,83.42,84.34,0.61
20260826,77.7,77.9,76.8,77.4,2553064,81.87,-5.46,83.19,84.13,0.49
20260827,78.1,78.5,77.5,77.5,2407979,81.51,-4.92,83.11,83.87,0.47
20260828,78.2,78.4,77.5,77.5,1778427,81.17,-4.53,82.88,83.63,0.36
20260831,77.5,78.1,76.9,77.2,2535881,80.84,-4.51,82.36,83.43,0.54
20260901,77.9,77.9,77.1,77.1,2276326,80.53,-4.26,81.76,83.22,0.48
20260902,77.5,77.5,76.8,76.8,1906533,80.22,-4.26,81.02,83.1,0.42
20260903,77.5,77.7,75,75.1,5028064,79.79,-5.88,80.19,82.94,1.08
20260904,75.1,75.8,74.4,75.6,2650839,79.44,-4.84,79.39,82.8,0.58
20260907,76,76,74.6,75.3,1632581,79.1,-4.8,78.48,82.61,0.37
20260908,75.7,75.8,73.3,73.5,4057357,78.63,-6.53,77.6,82.42,0.92
20260909,73.8,73.8,72.8,73,1989934,78.16,-6.6,77.13,82.19,0.56
20260910,73.2,73.2,71,71.1,3642279,77.57,-8.35,76.63,81.97,1.13
20260911,70.1,72.3,70,71.7,2030590,77.08,-6.99,76.22,81.75,0.7
20260914,71.4,71.8,70.7,71,1233523,76.58,-7.28,75.81,81.53,0.44
20260915,71.7,72.3,71.3,72,1657783,76.2,-5.51,75.5,81.36,0.63
20260916,72,72.8,71.3,71.9,1808126,75.84,-5.19,75.18,81.22,0.7
20260917,72.8,74,72.8,73.9,2093845,75.68,-2.35,75,81.09,0.85
20260918,74.6,74.6,73.2,73.6,1902797,75.5,-2.52,74.8,80.98,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 44.47
- over_600_ratio: 40.21
- over_800_ratio: 36.32
- over_1000_ratio: 34.87
- over_400_change_1w: 0.3
- over_800_change_1w: 0.42
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,50.24,-1.06,42.17,-0.79,40.2,-0.5,0,False,False
20260709,50.83,0.59,42.06,-0.11,40.04,-0.16,1,False,False
20260717,52.42,1.59,43.68,1.62,41.04,1,2,True,True
20260724,53.21,0.79,45.3,1.62,42.41,1.37,3,True,True
20260731,54.28,1.07,45.3,0,42.94,0.53,4,False,True
20260807,56.03,1.75,47.65,2.35,45.63,2.69,5,True,True
20260814,51.96,-4.07,44.03,-3.62,40.65,-4.98,0,False,False
20260821,48.65,-3.31,39.9,-4.13,36.71,-3.94,0,False,False
20260828,47.07,-1.58,38.81,-1.09,36.77,0.06,1,False,True
20260904,45.89,-1.18,37.46,-1.35,36.03,-0.74,0,False,False
20260911,44.17,-1.72,35.9,-1.56,34.76,-1.27,0,False,False
20260918,44.47,0.3,36.32,0.42,34.87,0.11,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 5388 | 中磊 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | no_signal | stale_signal | 1.董事會決議日期:NA 2.名稱﹝XX公司第X次（有、無）擔保公司債﹞: 中磊電子股份有限公司115年度第1次國內無擔保普通公司債 3.是否採總括申報發行公司債(是/否):否 4.發行總額:新臺幣25億元整 5.每張面額:新臺幣壹佰萬元整 6.發行價格:依票面金額十足發行 7.發行期間:3年期 8.發行利率:固定年利率2.70% 9.擔保品之種類、名稱、金額及約定事項:無 10.募得價款之用途及運用計畫:償還債務 11.承銷方式:委託證券承銷商以洽商銷售方式對外公開承銷 12.公司債受託人:中國信託商業銀行股份有限公司 13.承銷或代銷機構:委任富邦綜合證券股份有限公司為主辦承銷商 14.發行保證人:無 15.代理還本付息機構:合作金庫商業銀行南汐止分行 16.簽證機構:不適用 17.能轉換股份者，其轉換辦法:不適用 18.賣回條件:無 19.買回條件:無 20.附有轉換、交換或認股者，其換股基準日:不適用 21.附有轉換、交換或認股者，對股權可能稀釋情形:不適用 22.現金減資後再行募資之合理性及必要性 (募資當年度及前一年度有辦理現金減資者適用):不適用 23.其他應敘明事項: 本公司於115/5/12董事會通過募集國內普通公司債，此為完成115年度第1次國內 無擔保普通公司債定價後之說明。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 5388 | 中磊 | 3 | 3 | 4 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 5388 | 中磊 | 34 | 1 | 801580.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
