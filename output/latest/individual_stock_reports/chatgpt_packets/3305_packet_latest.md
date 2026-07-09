# INDIVIDUAL STOCK CHATGPT PACKET - 3305 昇貿

## Metadata
- generated_at: 2026-07-09 22:26:55 Asia/Taipei
- stock_id: 3305
- stock_name: 昇貿
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3305_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3305_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3305_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3305_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3305_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3305_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3305_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3305_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3305_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3305_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3305_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3305_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3305.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3305.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3305.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3305.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3305_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3305_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3305_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: high
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
- date: 20260709
- open: 131
- high: 134
- low: 127
- close: 127.5
- volume: 2480876
- ma5: 132.3
- ema23_primary: 136.99
- distance_to_ema23_pct: -6.93
- ma20: 137.5
- ma60: 133.85
- ma120: 122.48
- return_5d: -5.2
- return_20d: -6.59
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: -7.27
- distance_to_high_60_pct: -24.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,138,140.5,131,140,6544259,144.11,-2.85,150.03,124.32,0.51
20260612,145.5,149,143,144.5,6238423,144.14,0.25,150.32,124.92,0.52
20260615,147,148,143,144,3612818,144.13,-0.09,150.68,125.45,0.33
20260616,145,146.5,140,140.5,2987359,143.83,-2.31,150.8,125.98,0.32
20260617,140,143,138,142.5,1762137,143.72,-0.85,151.18,126.62,0.2
20260618,143,146,141,146,2759767,143.91,1.45,151.53,127.39,0.33
20260622,148.5,148.5,144.5,147,3945720,144.17,1.97,151.57,128.18,0.5
20260623,149.5,149.5,138,139,3598293,143.74,-3.29,150.5,128.78,0.49
20260624,135.5,138.5,135,138,1988362,143.26,-3.67,149.22,129.37,0.3
20260625,140,140.5,135,135,1954494,142.57,-5.31,147.97,129.84,0.32
20260626,134,137,128.5,129.5,3338157,141.48,-8.47,146.55,130.27,0.58
20260629,130.5,138,129,133.5,2620424,140.81,-5.19,145.35,130.71,0.48
20260630,136,140.5,135,139,2642000,140.66,-1.18,143.93,131.28,0.53
20260701,140.5,143,135.5,135.5,2287000,140.23,-3.38,142.82,131.84,0.51
20260702,134.5,138.5,131.5,134.5,1861000,139.76,-3.76,141.4,132.38,0.45
20260703,133,136.5,132,136,1331411,139.44,-2.47,140.2,132.82,0.33
20260706,137,141,134,136.5,1947000,139.2,-1.94,139.22,133.28,0.51
20260707,138.5,142.5,130,130.5,4275683,138.47,-5.76,138.5,133.52,1.14
20260708,133,140.5,128,131,5128880,137.85,-4.97,137.95,133.72,1.51
20260709,131,134,127,127.5,2480876,136.99,-6.93,137.5,133.85,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 49.03
- over_600_ratio: 46.65
- over_800_ratio: 44.78
- over_1000_ratio: 41.71
- over_400_change_1w: 0.15
- over_800_change_1w: 1.05
- over_1000_change_1w: -0.71
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,42.87,,37.09,,35.76,,0,False,False
20260508,44.41,1.54,39.03,1.94,37.75,1.99,1,True,True
20260515,48.07,3.66,44.39,5.36,39.49,1.74,2,True,True
20260522,47.52,-0.55,43.12,-1.27,40.61,1.12,3,False,True
20260529,50.41,2.89,45.2,2.08,43.87,3.26,4,True,True
20260605,50.79,0.38,46,0.8,44.2,0.33,5,False,True
20260612,49.18,-1.61,43.65,-2.35,42.4,-1.8,0,False,False
20260618,49.07,-0.11,43.54,-0.11,41.57,-0.83,0,False,False
20260626,48.88,-0.19,43.73,0.19,42.42,0.85,1,False,True
20260703,49.03,0.15,44.78,1.05,41.71,-0.71,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3305 | 昇貿 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  | no_signal | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 盈餘分配現金股利新台幣320,543,870元，每股配發新台幣2.3元。 3.變更後發放股利種類及金額: 盈餘分配現金股利新台幣320,543,870元，每股配發新台幣2.28330410元。 4.變更原因:因本公司可轉換公司債轉換普通股影響流通在外普通股股數總數， 故調整配息率。 5.其他應敘明事項:依115年03月12日董事會決議，授權董事長調整配息率相關事宜。；calendar event: ex_dividend on 20260715; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260709 | 3305 | 昇貿 | revenue_breakout_low_response | 營收爆發低反應股 | 11.0 | 38.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 盈餘分配現金股利新台幣320,543,870元，每股配發新台幣2.3元。 3.變更後發放股利種類及金額: 盈餘分配現金股利新台幣320,543,870元，每股配發新台幣2.28330410元。 4.變更原因:因本公司可轉換公司債轉換普通股影響流通在外普通股股數總數， 故調整配息率。 5.其他應敘明事項:依115年03月12日董事會決議，授權董事長調整配息率相關事宜。；calendar event: ex_dividend on 20260715; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3305 | 昇貿 | 22 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3305 | 昇貿 | 95 | 0 | 3959610.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
