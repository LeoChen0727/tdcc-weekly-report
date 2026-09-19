# INDIVIDUAL STOCK CHATGPT PACKET - 6691 洋基工程

## Metadata
- generated_at: 2026-09-19 22:17:27 Asia/Taipei
- stock_id: 6691
- stock_name: 洋基工程
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6691_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6691_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6691_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6691_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6691_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6691_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6691_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6691_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6691_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6691_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6691_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6691_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6691.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6691.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6691.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6691.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6691_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6691_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6691_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260918
- open: 619
- high: 650
- low: 617
- close: 650
- volume: 1363773
- ma5: 619.8
- ema23_primary: 631.75
- distance_to_ema23_pct: 2.89
- ma20: 617.9
- ma60: 680.53
- ma120: 664.47
- return_5d: 6.73
- return_20d: 9.61
- volume_ratio: 2.44
- distance_to_ma20_pct_auxiliary: 5.2
- distance_to_high_60_pct: -22.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,593,618,593,611,516771,686.01,-10.93,681.95,700.77,0.68
20260825,611,632,605,616,919908,680.18,-9.44,680.5,700.2,1.21
20260826,615,631,612,625,756632,675.58,-7.49,680.3,699.82,1.01
20260827,630,645,623,625,627449,671.37,-6.91,681.2,699.5,0.84
20260828,633,633,613,618,565056,666.92,-7.33,679.6,699.05,0.76
20260831,618,619,605,615,510605,662.59,-7.18,677.25,698.72,0.68
20260901,610,633,610,631,512218,659.96,-4.39,674.85,698.53,0.68
20260902,622,634,607,607,722931,655.55,-7.41,670.3,698.37,0.95
20260903,609,621,603,603,426141,651.17,-7.4,664.35,697.8,0.59
20260904,611,629,598,619,704992,648.49,-4.55,658.55,697.58,1
20260907,619,630,614,624,537844,646.45,-3.47,653.15,697.37,0.77
20260908,621,624,615,615,258676,643.83,-4.48,647.5,696.13,0.37
20260909,616,627,616,619,360316,641.76,-3.55,641.8,693.83,0.52
20260910,630,631,616,622,447277,640.11,-2.83,636.5,692.37,0.64
20260911,612,618,607,609,417102,637.52,-4.47,630.55,690.8,0.6
20260914,609,618,602,613,262367,635.47,-3.54,624.7,689.02,0.38
20260915,607,623,607,608,246634,633.19,-3.98,619.45,687.02,0.39
20260916,610,624,610,618,578902,631.92,-2.2,615.05,685.45,0.95
20260917,622,627,610,610,463671,630.09,-3.19,615.05,682.98,0.85
20260918,619,650,617,650,1363773,631.75,2.89,617.9,680.53,2.44
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 67.79
- over_600_ratio: 61.71
- over_800_ratio: 58.08
- over_1000_ratio: 54.27
- over_400_change_1w: 0.15
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,70.46,0.29,62.02,0.26,55.23,-1.28,7,False,True
20260709,70.1,-0.36,60.03,-1.99,55.5,0.27,8,False,True
20260717,69.47,-0.63,59.91,-0.12,54.67,-0.83,0,False,False
20260724,69.19,-0.28,59.76,-0.15,53.78,-0.89,0,False,False
20260731,68.36,-0.83,59.07,-0.69,53.78,0,0,False,False
20260807,69.17,0.81,60.08,1.01,54.79,1.01,1,True,True
20260814,69.74,0.57,59.12,-0.96,53.82,-0.97,2,False,False
20260821,68.44,-1.3,58.78,-0.34,54.22,0.4,3,False,True
20260828,68.08,-0.36,59.01,0.23,55.18,0.96,4,False,True
20260904,67.6,-0.48,58.07,-0.94,54.26,-0.92,0,False,False
20260911,67.64,0.04,58.08,0.01,54.27,0.01,1,False,True
20260918,67.79,0.15,58.08,0,54.27,0,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6691 | 洋基工程 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | call_strong_inflow | first_seen | 符合條款第四條第XX款：12 事實發生日：115/09/24 1.召開法人說明會之日期：115/09/24 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：臺北市大安區仁愛路四段169號15樓（富邦金融大樓） 4.法人說明會擇要訊息：公告本公司受邀參加富邦綜合證券舉辦之法人說明會 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6691 | 洋基工程 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  | call_strong_inflow | first_seen | 符合條款第四條第XX款：12 事實發生日：115/09/24 1.召開法人說明會之日期：115/09/24 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：臺北市大安區仁愛路四段169號15樓（富邦金融大樓） 4.法人說明會擇要訊息：公告本公司受邀參加富邦綜合證券舉辦之法人說明會 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260918 | 6691 | 洋基工程 | revenue_breakout_low_response | 營收爆發低反應股 | 22 | 5 | B_可等確認_營建認列型需基本面確認 |  |  | call_strong_inflow | first_seen | 符合條款第四條第XX款：12 事實發生日：115/09/24 1.召開法人說明會之日期：115/09/24 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：臺北市大安區仁愛路四段169號15樓（富邦金融大樓） 4.法人說明會擇要訊息：公告本公司受邀參加富邦綜合證券舉辦之法人說明會 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260918 | 6691 | 洋基工程 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  | call_strong_inflow | first_seen | 符合條款第四條第XX款：12 事實發生日：115/09/24 1.召開法人說明會之日期：115/09/24 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：臺北市大安區仁愛路四段169號15樓（富邦金融大樓） 4.法人說明會擇要訊息：公告本公司受邀參加富邦綜合證券舉辦之法人說明會 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6691 | 洋基工程 | 1 | 1 | 1 | 1 | 3 | first_seen | 首次上榜或資料有限，需後續確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6691 | 洋基工程 | 44 | 1 | 7967820.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
