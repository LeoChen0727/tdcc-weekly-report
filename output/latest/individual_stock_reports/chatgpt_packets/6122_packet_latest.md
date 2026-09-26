# INDIVIDUAL STOCK CHATGPT PACKET - 6122 擎邦

## Metadata
- generated_at: 2026-09-26 15:52:46 Asia/Taipei
- stock_id: 6122
- stock_name: 擎邦
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6122_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6122_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6122.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6122.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6122.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6122.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6122_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6122_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6122_latest.md?ref=main

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
- action_rating_display_zh: 可小量試單
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 嚴格突破，價格結構尚未破壞，操作評級為「可小量試單」。
- entry_strategy_zh: 突破後順勢追蹤；可依「試單 1/3 部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 試單 1/3 部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 嚴格突破，價格結構尚未破壞，操作評級為「可小量試單」。 進場策略：突破後順勢追蹤；可依「試單 1/3 部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: starter_position
- action_rating_label_zh: 可小量試單
- confidence_level: medium
- thesis_state: breakout_confirmed
- entry_style: breakout_follow
- position_sizing: starter_1_3

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
- open: 54.2
- high: 58.5
- low: 53.6
- close: 58.2
- volume: 2682000
- ma5: 53.84
- ema23_primary: 51.42
- distance_to_ema23_pct: 13.18
- ma20: 51.19
- ma60: 49.88
- ma120: 49.16
- return_5d: 13.45
- return_20d: 19.51
- volume_ratio: 4.44
- distance_to_ma20_pct_auxiliary: 13.71
- distance_to_high_60_pct: -0.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,48.7,48.9,48.4,48.65,153000,48.25,0.83,47.48,48.66,0.72
20260831,48.5,48.5,47.8,48,108000,48.23,-0.47,47.55,48.65,0.54
20260901,48,48.55,48,48.05,92000,48.21,-0.34,47.66,48.64,0.49
20260902,47.7,49,47.65,48.7,137000,48.25,0.92,47.8,48.66,0.74
20260903,50.6,52.4,49.5,51.9,2005000,48.56,6.88,48.06,48.73,7.38
20260904,52.4,52.5,51.2,51.3,876000,48.79,5.15,48.27,48.79,2.89
20260907,51.1,51.6,50.2,51.5,326000,49.01,5.08,48.47,48.88,1.06
20260908,51.5,51.5,50.5,50.5,160000,49.14,2.78,48.66,48.95,0.53
20260909,50.8,51,49.5,50.5,312000,49.25,2.54,48.85,49,1
20260910,51.2,51.2,50,50.4,148000,49.35,2.14,49.02,49.05,0.49
20260911,50.2,51,49.8,50.8,256000,49.47,2.69,49.2,49.12,0.82
20260914,50.8,51.8,50.7,51.1,333000,49.6,3.02,49.37,49.19,1.06
20260915,51.5,51.5,50.7,50.7,248000,49.69,2.02,49.5,49.24,0.79
20260916,50.8,51.3,50.5,51.1,185000,49.81,2.59,49.69,49.32,0.59
20260917,51.6,51.6,50.8,51.3,299000,49.94,2.73,49.87,49.38,0.92
20260918,51.5,51.7,50.6,51.2,278000,50.04,2.32,50.03,49.43,0.83
20260921,51.2,52.3,51,51.7,410000,50.18,3.03,50.19,49.51,1.2
20260922,52.3,53,51.6,52.9,903000,50.41,4.95,50.38,49.6,2.4
20260923,53.1,55.4,53,55.2,2160000,50.81,8.65,50.71,49.72,4.5
20260924,54.2,58.5,53.6,58.2,2682000,51.42,13.18,51.19,49.88,4.44
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 35.33
- over_600_ratio: 32.97
- over_800_ratio: 26.64
- over_1000_ratio: 23.14
- over_400_change_1w: 2.4
- over_800_change_1w: 1.24
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 13
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,30.79,1.22,22.88,0.02,20.52,0.02,2,True,True
20260717,31.65,0.86,24.24,1.36,21.88,1.36,3,True,True
20260724,31.55,-0.1,24.27,0.03,21.91,0.03,4,False,True
20260731,30.99,-0.56,24.28,0.01,21.92,0.01,5,False,True
20260807,31.1,0.11,24.39,0.11,22.03,0.11,6,True,True
20260814,31.15,0.05,24.44,0.05,22.08,0.05,7,True,True
20260821,31.15,0,24.46,0.02,22.1,0.02,8,False,True
20260828,30.75,-0.4,24.6,0.14,22.24,0.14,9,False,True
20260904,31.99,1.24,24.64,0.04,22.28,0.04,10,True,True
20260911,32.23,0.24,24.79,0.15,22.43,0.15,11,True,True
20260918,32.93,0.7,25.4,0.61,23.04,0.61,12,True,True
20260924,35.33,2.4,26.64,1.24,23.14,0.1,13,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6122 | 擎邦 | true_breakout | 嚴格突破 | 126.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.事實發生日:115/09/02 2.契約或承諾相對人: 台塑新智能科技股份有限公司 3.與公司關係:業主 4.契約或承諾起迄日期（或解除日期）:施工期限為決標後455日， 契約待業主董事會決議通過後，由雙方完成正式契約簽署後確定。 5.主要內容（解除者不適用）:本公司收到台塑新智能科技股份有限公司 之彰濱廠二期營建統包及機電設計案之得標通知，得標通知所載未稅金額 約為新臺幣陸拾參億捌仟多萬元。本案尚待業主董事會決議通過後始生效， 實際權利義務以雙方後續簽署之正式契約為準。 6.限制條款（解除者不適用）:尚待正式契約簽訂後確定 7.承諾事項（解除者不適用）:尚待正式契約簽訂後確定 8.其他重要約定事項（解除者不適用）:無 9.對公司財務、業務之影響: 本案如後續正式生效並依約履行，預期將充實本公司在建工程規模及 未來營收動能，對本公司未來營收及獲利表現具正面貢獻。 10.具體目的:拓展工程承攬業務。 11.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項): 本公司依業主得標通知書辦理公告。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6122 | 擎邦 | 2 | 2 | 2 | 2 | 3 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
