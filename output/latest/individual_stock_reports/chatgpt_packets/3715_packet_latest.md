# INDIVIDUAL STOCK CHATGPT PACKET - 3715 定穎投控

## Metadata
- generated_at: 2026-08-22 16:00:20 Asia/Taipei
- stock_id: 3715
- stock_name: 定穎投控
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3715_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3715_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3715_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3715_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3715.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3715.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3715.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3715.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3715_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3715_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3715_latest.md?ref=main

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
- date: 20260821
- open: 109.5
- high: 109.5
- low: 107
- close: 107
- volume: 1813015
- ma5: 109.8
- ema23_primary: 117.22
- distance_to_ema23_pct: -8.72
- ma20: 110.22
- ma60: 143.77
- ma120: 159.64
- return_5d: -7.76
- return_20d: -8.15
- volume_ratio: 0.3
- distance_to_ma20_pct_auxiliary: -2.92
- distance_to_high_60_pct: -45.55

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,116.5,116.5,109.5,114,4970547,142.06,-19.75,144.65,165.25,0.73
20260728,110,110,103.5,104,5475074,138.89,-25.12,141.55,164.08,0.8
20260729,106,106,93.6,98,10588104,135.48,-27.66,137.65,162.73,1.5
20260730,98,101,89.5,90.9,8149741,131.76,-31.01,133.59,160.97,1.17
20260731,99.5,99.9,97.6,99.9,3869810,129.11,-22.62,129.81,159.53,0.56
20260803,99.9,107,99.9,104.5,4464229,127.06,-17.75,126.44,158.12,0.64
20260804,102,107.5,99.7,104.5,6384991,125.18,-16.52,123.42,156.85,0.95
20260805,107,113,105.5,109.5,7350549,123.87,-11.6,121.11,155.66,1.13
20260806,109.5,120,106,116.5,9057965,123.26,-5.48,119.36,154.59,1.41
20260807,116,117.5,113,114.5,5593699,122.53,-6.55,117.54,153.56,0.88
20260810,119,125.5,118.5,125.5,4961217,122.78,2.22,116.61,152.63,0.8
20260811,124.5,129,122,122,12494182,122.71,-0.58,115.67,151.75,1.96
20260812,118.5,119.5,117,118,7082626,122.32,-3.53,114.44,150.87,1.09
20260813,119,122,117.5,117.5,6303302,121.92,-3.62,113.47,150.08,0.95
20260814,118,119,115,116,4353421,121.42,-4.47,113.09,149.33,0.69
20260817,114.5,116,111,115,6106615,120.89,-4.87,112.86,148.51,0.97
20260818,115,115,110,110,3518394,119.98,-8.32,112.24,147.44,0.56
20260819,107,112.5,106,107.5,4364586,118.94,-9.62,111.34,146.25,0.7
20260820,109.5,110.5,107,109.5,1972458,118.15,-7.32,110.69,144.97,0.32
20260821,109.5,109.5,107,107,1813015,117.22,-8.72,110.22,143.77,0.3
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 29.2
- over_600_ratio: 25.78
- over_800_ratio: 23.34
- over_1000_ratio: 20.83
- over_400_change_1w: -0.01
- over_800_change_1w: 0.43
- over_1000_change_1w: 0.13
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,32.13,-1.78,26.2,-2.4,23.99,-2.18,0,False,False
20260612,32.19,0.06,27.09,0.89,25.17,1.18,1,True,True
20260618,34.4,2.21,29.16,2.07,27.85,2.68,2,True,True
20260626,38.37,3.97,32.04,2.88,31.09,3.24,3,True,True
20260703,36.61,-1.76,30.92,-1.12,29.98,-1.11,0,False,False
20260709,31.82,-4.79,25.82,-5.1,23.24,-6.74,0,False,False
20260717,29.9,-1.92,24.04,-1.78,21.79,-1.45,0,False,False
20260724,29.38,-0.52,24.26,0.22,21.11,-0.68,1,False,True
20260731,29.75,0.37,24.34,0.08,21.47,0.36,2,False,True
20260807,29.59,-0.16,24.54,0.2,22.01,0.54,3,False,True
20260814,29.21,-0.38,22.91,-1.63,20.7,-1.31,0,False,False
20260821,29.2,-0.01,23.34,0.43,20.83,0.13,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3715 | 定穎投控 | revenue_pullback | 營收成長股價回檔 | 64.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/08/19 2.公司名稱:定穎電子(昆山)有限公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:間接持股86.0989% 5.發生緣由:代子公司更正115年5-7月衍生性商品交易資訊 6.更正資訊項目/報表名稱:115年5-7月衍生性商品交易資訊 7.更正前金額/內容/頁次: 115年5月遠期契約，未沖銷契約公允價值:93,342仟元 115年6月遠期契約，未沖銷契約公允價值:189,540仟元 115年7月遠期契約，未沖銷契約公允價值:192,513仟元 8.更正後金額/內容/頁次: 115年5月遠期契約，未沖銷契約公允價值:46仟元 115年6月遠期契約，未沖銷契約公允價值:-831仟元 115年7月遠期契約，未沖銷契約公允價值:-43仟元 9.因應措施:更正後內容上傳公開資訊觀測站 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 3715 | 定穎投控 | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 48 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.事實發生日:115/08/19 2.公司名稱:定穎電子(昆山)有限公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:間接持股86.0989% 5.發生緣由:代子公司更正115年5-7月衍生性商品交易資訊 6.更正資訊項目/報表名稱:115年5-7月衍生性商品交易資訊 7.更正前金額/內容/頁次: 115年5月遠期契約，未沖銷契約公允價值:93,342仟元 115年6月遠期契約，未沖銷契約公允價值:189,540仟元 115年7月遠期契約，未沖銷契約公允價值:192,513仟元 8.更正後金額/內容/頁次: 115年5月遠期契約，未沖銷契約公允價值:46仟元 115年6月遠期契約，未沖銷契約公允價值:-831仟元 115年7月遠期契約，未沖銷契約公允價值:-43仟元 9.因應措施:更正後內容上傳公開資訊觀測站 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3715 | 定穎投控 | 4 | 4 | 4 | 4 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3715 | 定穎投控 | 218 | 6 | 1338030.0 | 62540.0 | 21.39 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
