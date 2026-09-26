# INDIVIDUAL STOCK CHATGPT PACKET - 6139 亞翔

## Metadata
- generated_at: 2026-09-26 15:52:47 Asia/Taipei
- stock_id: 6139
- stock_name: 亞翔
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6139_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6139_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6139_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6139_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6139_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6139_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6139_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6139_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6139_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6139_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6139_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6139_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6139.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6139.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6139.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6139.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6139_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6139_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6139_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260924
- open: 733
- high: 755
- low: 725
- close: 753
- volume: 3399157
- ma5: 731
- ema23_primary: 738.61
- distance_to_ema23_pct: 1.95
- ma20: 731.8
- ma60: 783.22
- ma120: 763.28
- return_5d: 8.19
- return_20d: -3.95
- volume_ratio: 1.43
- distance_to_ma20_pct_auxiliary: 2.9
- distance_to_high_60_pct: -23.71

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,788,792,772,775,2585203,786.17,-1.42,789.55,813.4,0.9
20260831,768,768,737,755,3030230,783.57,-3.65,789.05,812.23,1.11
20260901,757,780,757,770,1963615,782.44,-1.59,788.25,811.6,0.75
20260902,755,767,718,721,4516304,777.32,-7.25,784.3,811.48,1.67
20260903,725,741,711,712,2059979,771.88,-7.76,778.1,810.87,0.8
20260904,722,745,703,736,2366253,768.89,-4.28,774.8,810.85,0.93
20260907,740,745,734,739,1612698,766.4,-3.57,771.35,810.97,0.67
20260908,744,753,739,742,1159350,764.36,-2.93,767.85,809.92,0.51
20260909,748,762,746,750,1607925,763.17,-1.73,764.8,807.67,0.72
20260910,748,759,735,753,1324647,762.32,-1.22,762.2,806.68,0.62
20260911,742,744,709,709,3092463,757.88,-6.45,757.75,805.07,1.42
20260914,704,717,695,703,1351218,753.3,-6.68,752.55,803.07,0.63
20260915,701,726,701,713,2055879,749.94,-4.93,749.1,801.45,0.97
20260916,713,722,707,707,1697549,746.37,-5.27,746.15,800.05,0.82
20260917,711,722,696,696,2157163,742.17,-6.22,742.65,798.02,1.04
20260918,706,734,706,733,4528809,741.4,-1.13,741.2,795.65,2
20260921,740,745,717,718,1725029,739.45,-2.9,739.2,792.98,0.75
20260922,729,731,715,715,1640135,737.42,-3.04,736.55,788.98,0.72
20260923,725,750,720,736,3750210,737.3,-0.18,733.35,785.87,1.59
20260924,733,755,725,753,3399157,738.61,1.95,731.8,783.22,1.43
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 62.45
- over_600_ratio: 57.83
- over_800_ratio: 56.17
- over_1000_ratio: 51.36
- over_400_change_1w: 0.19
- over_800_change_1w: 0.18
- over_1000_change_1w: -0.36
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,69.04,-0.51,61.58,-1.56,57.63,-1.22,0,False,False
20260717,68.14,-0.9,60.92,-0.66,56.24,-1.39,0,False,False
20260724,67.61,-0.53,59.83,-1.09,55.03,-1.21,0,False,False
20260731,65.68,-1.93,56.52,-3.31,52.2,-2.83,0,False,False
20260807,66.08,0.4,57.64,1.12,53.31,1.11,1,True,True
20260814,65.1,-0.98,57.14,-0.5,52.84,-0.47,0,False,False
20260821,64.52,-0.58,57.43,0.29,51.64,-1.2,1,False,True
20260828,64.81,0.29,57.81,0.38,52.83,1.19,2,True,True
20260904,63.64,-1.17,56.07,-1.74,52.58,-0.25,0,False,False
20260911,63.35,-0.29,56.53,0.46,51.86,-0.72,1,False,True
20260918,62.26,-1.09,55.99,-0.54,51.72,-0.14,0,False,False
20260924,62.45,0.19,56.17,0.18,51.36,-0.36,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6139 | 亞翔 | pullback_rebound | 回檔後短線轉強 | 62.0 |  |  |  |  | call_put_bullish | stale_signal | 1.董事會、股東會決議或公司決定日期:115/09/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放股利種類及金額:現金股利人民幣352,044,000元 4.除權（息）交易日:NA 5.最後過戶日:NA 6.停止過戶起始日期:NA 7.停止過戶截止日期:NA 8.除權（息）基準日:115/09/15 9.其他應敘明事項: 每股配發現金紅利1.65元(人民幣) 股權登記日：115/09/14 現金紅利發放日：115/09/15；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 6139 | 亞翔 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | call_put_bullish | stale_signal | 1.董事會、股東會決議或公司決定日期:115/09/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放股利種類及金額:現金股利人民幣352,044,000元 4.除權（息）交易日:NA 5.最後過戶日:NA 6.停止過戶起始日期:NA 7.停止過戶截止日期:NA 8.除權（息）基準日:115/09/15 9.其他應敘明事項: 每股配發現金紅利1.65元(人民幣) 股權登記日：115/09/14 現金紅利發放日：115/09/15；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 6139 | 亞翔 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 67.0 |  |  | neckline_challenge |  | call_put_bullish | stale_signal | 1.董事會、股東會決議或公司決定日期:115/09/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放股利種類及金額:現金股利人民幣352,044,000元 4.除權（息）交易日:NA 5.最後過戶日:NA 6.停止過戶起始日期:NA 7.停止過戶截止日期:NA 8.除權（息）基準日:115/09/15 9.其他應敘明事項: 每股配發現金紅利1.65元(人民幣) 股權登記日：115/09/14 現金紅利發放日：115/09/15；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6139 | 亞翔 | 5 | 5 | 5 | 8 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6139 | 亞翔 | 244 | 1 | 44854990.0 | 1270.0 | 35318.89 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
