# INDIVIDUAL STOCK CHATGPT PACKET - 3498 陽程

## Metadata
- generated_at: 2026-08-01 15:53:39 Asia/Taipei
- stock_id: 3498
- stock_name: 陽程
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3498_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3498_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3498.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3498.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3498.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3498.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3498_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3498_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3498_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260730
- open: 91.5
- high: 94.1
- low: 84.1
- close: 86.3
- volume: 1239000
- ma5: 99.66
- ema23_primary: 112.05
- distance_to_ema23_pct: -22.98
- ma20: 114.97
- ma60: 124.14
- ma120: 96.52
- return_5d: -24.63
- return_20d: -27.48
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: -24.93
- distance_to_high_60_pct: -47.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,117,127.5,116,123,1659000,122.52,0.4,122.03,114.57,1.31
20260703,123,124.5,120.5,124,966000,122.64,1.11,121.6,115.36,0.74
20260706,125.5,128,124,124,1114000,122.75,1.02,121.28,116.03,0.82
20260707,125.5,136,122.5,123,5016000,122.77,0.18,121.05,116.75,3.45
20260708,124,130.5,116.5,119.5,3647000,122.5,-2.45,120.42,117.28,2.39
20260709,124,131,124,126.5,4601000,122.83,2.98,120.6,117.96,2.76
20260713,136,139,128.5,131,7067000,123.51,6.06,121.38,118.78,3.85
20260714,140,140,118,119.5,4597000,123.18,-2.99,121.3,119.41,2.29
20260715,119.5,128,119.5,123,1765000,123.16,-0.13,121.17,120.05,0.87
20260716,122,131.5,119,129.5,2216000,123.69,4.7,121.62,120.78,1.07
20260717,124.5,125.5,117,117,2487000,123.14,-4.98,121.53,121.27,1.15
20260720,113.5,115,105.5,109.5,1784000,122,-10.24,120.85,121.65,0.81
20260721,109.5,113,103.5,105.5,1733000,120.62,-12.54,119.97,122.08,0.78
20260722,107.5,112.5,106.5,111.5,1477000,119.86,-6.98,119.62,122.64,0.66
20260723,111.5,115.5,108.5,114.5,1063000,119.42,-4.12,119.22,123.26,0.47
20260724,113,115,109.5,111.5,901000,118.76,-6.11,118.88,123.78,0.4
20260727,111,112,106.5,108,621000,117.86,-8.37,118.62,124.25,0.28
20260728,105,106,99.2,99.2,2859000,116.31,-14.71,117.86,124.44,1.22
20260729,101,101,89.3,93.3,2622000,114.39,-18.44,116.6,124.39,1.07
20260730,91.5,94.1,84.1,86.3,1239000,112.05,-22.98,114.97,124.14,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 48.4
- over_600_ratio: 46.86
- over_800_ratio: 42.14
- over_1000_ratio: 42.14
- over_400_change_1w: -0.01
- over_800_change_1w: -1.83
- over_1000_change_1w: 2.32
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,51.96,6.93,47.64,4.3,46.04,5.61,1,True,True
20260522,54.51,2.55,51.9,4.26,49.07,3.03,2,True,True
20260529,54.6,0.09,50.24,-1.66,48.83,-0.24,3,False,False
20260605,52.18,-2.42,47.69,-2.55,47.69,-1.14,0,False,False
20260612,51.42,-0.76,47.35,-0.34,47.35,-0.34,0,False,False
20260618,51.39,-0.03,46.76,-0.59,45.14,-2.21,0,False,False
20260626,50.6,-0.79,47.72,0.96,45.01,-0.13,1,False,True
20260703,51.84,1.24,48.31,0.59,46.89,1.88,2,True,True
20260709,49.16,-2.68,43.94,-4.37,43.94,-2.95,0,False,False
20260717,48.9,-0.26,42.29,-1.65,39.52,-4.42,0,False,False
20260724,48.41,-0.49,43.97,1.68,39.82,0.3,1,False,True
20260731,48.4,-0.01,42.14,-1.83,42.14,2.32,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3498 | 陽程 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.法律事件之當事人:上海陽程科技有限公司 2.法律事件之法院名稱或處分機關:河南省林州市人民法院 3.法律事件之相關文書案號:河南省林州市人民法院判決書                        （2025）豫0581民初7776號 4.事實發生日:115/07/09 5.發生原委(含爭訟標的):本公司之子公司上海陽程科技有限公司於2020年9月委由 北京市道成律師事務所，處理上海陽程科技有限公司與林州致遠電子科技有限公司間 承攬合同糾紛案說判決說明。 判決結果： 我方總計須在判決生效後 15 日內支付給原告人民幣23,998,347.23元，明細如下： ‧賠償金：人民幣23,163,739.23元（含已維修費、未維修貶值、停產及品質損失）。 ‧鑑定費：人民幣689,900元。 ‧案件受理費：人民幣139,708元。 ‧保全申請費：人民幣5,000元。 6.處理過程:提出上訴並持續與律師溝通。 7.對公司財務業務影響及預估影響金額:本案本公司已提列足額損失準備， 對財務業務無重大影響。因先前對造超額聲請財產保全應付予本公司貨款， 若依本次判決結果，本公司可聲請發還約人民幣789萬元之款項。 8.因應措施及改善情形: 本公司認為，原審裁判結果顯流於地方保護主義，對於本公司提出之多處明顯爭點未予 審酌，更刻意迴避訴訟時效等重大法律事實，在無法律依據下全盤採納對造主張，其 認事用法顯失公正。 為維護本公司權益擬提起上訴。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第2款所定對 股東權益或證券價格有重大影響之事項):不適用；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3498 | 陽程 | 9 | 2 | 5 | 9 | 12 | repeated_but_no_breakout | 近 10 日上榜 9 次、近 20 日上榜 12 次，但尚未有效突破，需等待攻擊確認。 |

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
