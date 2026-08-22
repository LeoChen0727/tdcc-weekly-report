# INDIVIDUAL STOCK CHATGPT PACKET - 3702 大聯大

## Metadata
- generated_at: 2026-08-22 16:00:19 Asia/Taipei
- stock_id: 3702
- stock_name: 大聯大
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3702_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3702_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3702_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3702_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3702.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3702.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3702.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3702.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3702_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3702_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3702_latest.md?ref=main

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
- date: 20260821
- open: 104.5
- high: 111.5
- low: 104.5
- close: 111
- volume: 12845812
- ma5: 107.9
- ema23_primary: 114.43
- distance_to_ema23_pct: -3
- ma20: 115.83
- ma60: 113.01
- ma120: 104.49
- return_5d: -3.48
- return_20d: -5.53
- volume_ratio: 1.1
- distance_to_ma20_pct_auxiliary: -4.17
- distance_to_high_60_pct: -14.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,118,118.5,113.5,116,5956267,112.84,2.8,111.88,111.89,0.41
20260728,113.5,114,109,110,7135143,112.61,-2.32,112.15,112.04,0.5
20260729,110.5,110.5,102.5,106,8994110,112.06,-5.41,112.1,112.07,0.64
20260730,105,108,102,105.5,11099586,111.51,-5.39,111.88,112.12,0.93
20260731,110.5,113.5,109.5,112.5,12300466,111.59,0.81,112.1,112.26,1.05
20260803,111,117.5,109,116,6938127,111.96,3.61,112.4,112.47,0.59
20260804,113.5,120.5,113.5,117.5,8678579,112.42,4.52,112.78,112.53,0.74
20260805,119,129,119,129,17747015,113.8,13.35,113.78,112.78,1.47
20260806,126.5,127,122.5,125.5,15203415,114.78,9.34,114.78,112.97,1.21
20260807,126.5,127,121,122.5,9985739,115.42,6.13,115.58,113.17,0.79
20260810,123,130.5,123,130,11702194,116.64,11.46,116.22,113.49,0.92
20260811,126,128,121,125.5,12205592,117.38,6.92,116.53,113.75,1.02
20260812,125,125.5,121,122.5,14569285,117.8,3.99,116.83,113.95,1.26
20260813,122.5,125,120.5,123.5,10898881,118.28,4.42,117.33,114.2,0.95
20260814,124.5,124.5,115,115,12191511,118,-2.55,117.6,114.13,1.06
20260817,114.5,116,109.5,111,11002940,117.42,-5.47,117.83,113.92,0.96
20260818,110.5,111,106,106.5,10734022,116.51,-8.59,117.58,113.73,0.93
20260819,106,107.5,103,106.5,18979455,115.68,-7.93,117,113.45,1.59
20260820,108,109.5,103,104.5,14688136,114.74,-8.93,116.15,113.17,1.23
20260821,104.5,111.5,104.5,111,12845812,114.43,-3,115.83,113.01,1.1
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 83.66
- over_600_ratio: 81.67
- over_800_ratio: 79.99
- over_1000_ratio: 78.76
- over_400_change_1w: -1.16
- over_800_change_1w: -0.99
- over_1000_change_1w: -1.07
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,84.99,-0.25,81.56,-0.29,80.31,-0.32,0,False,False
20260612,84.76,-0.23,81.28,-0.28,80.14,-0.17,0,False,False
20260618,84.37,-0.39,80.5,-0.78,79.57,-0.57,0,False,False
20260626,84.2,-0.17,80.34,-0.16,79.22,-0.35,0,False,False
20260703,84.22,0.02,80,-0.34,79.02,-0.2,1,False,False
20260709,83.99,-0.23,80.09,0.09,78.96,-0.06,2,False,True
20260717,84.1,0.11,80.35,0.26,79.03,0.07,3,True,True
20260724,84.53,0.43,80.59,0.24,79.34,0.31,4,True,True
20260731,84.57,0.04,80.69,0.1,79.45,0.11,5,False,True
20260807,85.05,0.48,81.13,0.44,80.06,0.61,6,True,True
20260814,84.82,-0.23,80.98,-0.15,79.83,-0.23,0,False,False
20260821,83.66,-1.16,79.99,-0.99,78.76,-1.07,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3702 | 大聯大 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  | call_inflow | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:大聯大控股(股)公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司115年7月份自結合併營收 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 隨著全球科技產業與下游客戶加速推進科技升級與能源基礎設施建置，強勁的企業資 本支出帶動半導體及電子零組件的廣泛拉貨動能。除了電源管理、伺服器、網通設備 、儲能系統及高密度連接元件展現強勁拉貨動能，車用電子與工業控制需求亦穩步推 進，此外，智能倉儲管理與資訊系統整合等高附加價值服務需求同步擴增；各市場多 元終端應用與軟硬體服務的雙軌並進，為公司營運挹注穩健且具持續性的結構性成長 動能。 在此趨勢推升，加上公司持續深化供應鏈整合與全球營運布局下，大聯大2026年7月 合併營收為新台幣1,461億元，較去年同期大幅成長90.8%。累計營收達新台幣 9,208.7億元，較去年同期成長59.9%，並達2025年全年營收之九成，展現強勁的成 長動能。；calendar event: ex_dividend on 20260827; status=confirmed; proximity=within_7d |
| 20260821 | 3702 | 大聯大 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  | call_inflow | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:大聯大控股(股)公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司115年7月份自結合併營收 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 隨著全球科技產業與下游客戶加速推進科技升級與能源基礎設施建置，強勁的企業資 本支出帶動半導體及電子零組件的廣泛拉貨動能。除了電源管理、伺服器、網通設備 、儲能系統及高密度連接元件展現強勁拉貨動能，車用電子與工業控制需求亦穩步推 進，此外，智能倉儲管理與資訊系統整合等高附加價值服務需求同步擴增；各市場多 元終端應用與軟硬體服務的雙軌並進，為公司營運挹注穩健且具持續性的結構性成長 動能。 在此趨勢推升，加上公司持續深化供應鏈整合與全球營運布局下，大聯大2026年7月 合併營收為新台幣1,461億元，較去年同期大幅成長90.8%。累計營收達新台幣 9,208.7億元，較去年同期成長59.9%，並達2025年全年營收之九成，展現強勁的成 長動能。；calendar event: ex_dividend on 20260827; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 3702 | 大聯大 | revenue_breakout_low_response | 營收爆發低反應股 | 21 | 10 | A_優先追蹤 |  |  | call_inflow | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:大聯大控股(股)公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司115年7月份自結合併營收 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 隨著全球科技產業與下游客戶加速推進科技升級與能源基礎設施建置，強勁的企業資 本支出帶動半導體及電子零組件的廣泛拉貨動能。除了電源管理、伺服器、網通設備 、儲能系統及高密度連接元件展現強勁拉貨動能，車用電子與工業控制需求亦穩步推 進，此外，智能倉儲管理與資訊系統整合等高附加價值服務需求同步擴增；各市場多 元終端應用與軟硬體服務的雙軌並進，為公司營運挹注穩健且具持續性的結構性成長 動能。 在此趨勢推升，加上公司持續深化供應鏈整合與全球營運布局下，大聯大2026年7月 合併營收為新台幣1,461億元，較去年同期大幅成長90.8%。累計營收達新台幣 9,208.7億元，較去年同期成長59.9%，並達2025年全年營收之九成，展現強勁的成 長動能。；calendar event: ex_dividend on 20260827; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3702 | 大聯大 | 6 | 6 | 5 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3702 | 大聯大 | 47 | 0 | 2702710.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
