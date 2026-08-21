# INDIVIDUAL STOCK CHATGPT PACKET - 5388 中磊

## Metadata
- generated_at: 2026-08-21 22:27:45 Asia/Taipei
- stock_id: 5388
- stock_name: 中磊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260821
- open: 77.9
- high: 78.4
- low: 77.5
- close: 77.6
- volume: 2412760
- ma5: 78.2
- ema23_primary: 83.22
- distance_to_ema23_pct: -6.75
- ma20: 84.53
- ma60: 84.62
- ma120: 82.42
- return_5d: -2.76
- return_20d: -12.51
- volume_ratio: 0.4
- distance_to_ma20_pct_auxiliary: -8.2
- distance_to_high_60_pct: -18.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,89.8,94.7,89.7,90.6,10755390,85.32,6.19,84.31,83.77,2.21
20260728,88.2,90,86.2,86.4,4970904,85.41,1.16,84.77,83.93,0.99
20260729,87.6,87.8,79.2,81.9,7966935,85.11,-3.78,84.82,84,1.51
20260730,81.4,82.1,78.8,79.1,4462046,84.61,-6.52,84.8,84,0.83
20260731,83.2,84.3,81.5,82.3,6868763,84.42,-2.51,84.89,84.06,1.24
20260803,82.3,88.5,81.7,87.4,5776546,84.67,3.23,85.17,84.18,1.01
20260804,86.4,89.6,86.3,89.2,2752969,85.05,4.88,85.56,84.25,0.48
20260805,90,92.8,89.7,91.6,5001820,85.59,7.02,85.97,84.32,0.93
20260806,91.3,92.2,89.9,91.8,2815297,86.11,6.61,86.41,84.38,0.52
20260807,94.6,95,90.5,91.4,5068086,86.55,5.6,86.75,84.58,0.96
20260810,93.1,94.7,90.7,93.6,4818108,87.14,7.42,87.16,84.85,0.9
20260811,93.6,94.1,91,91.1,3697798,87.47,4.15,87.43,85.07,0.7
20260812,88.7,88.7,82,82.4,19410824,87.05,-5.34,87.08,85.15,3.46
20260813,82.3,82.4,80.4,81.1,9499354,86.55,-6.3,86.81,85.18,1.63
20260814,81.2,81.2,79.2,79.8,8550021,85.99,-7.2,86.63,85.15,1.42
20260817,80.8,80.8,78.9,79.3,3598243,85.43,-7.18,86.45,85.08,0.59
20260818,79.8,80,78.1,78.1,4471274,84.82,-7.92,86.11,84.97,0.73
20260819,77.4,79.2,77,78.4,3304135,84.28,-6.98,85.67,84.83,0.54
20260820,79.4,79.4,77.3,77.6,4463556,83.73,-7.32,85.09,84.72,0.73
20260821,77.9,78.4,77.5,77.6,2412760,83.22,-6.75,84.53,84.62,0.4
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 51.96
- over_600_ratio: 47.39
- over_800_ratio: 44.03
- over_1000_ratio: 40.65
- over_400_change_1w: -4.07
- over_800_change_1w: -3.62
- over_1000_change_1w: -4.98
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,53.66,2.55,45.5,2.02,43.47,2.58,2,True,True
20260605,53.05,-0.61,45.13,-0.37,42.86,-0.61,0,False,False
20260612,53.14,0.09,44.3,-0.83,42.31,-0.55,1,False,False
20260618,52.36,-0.78,43.7,-0.6,42.3,-0.01,0,False,False
20260626,51.3,-1.06,42.96,-0.74,40.7,-1.6,0,False,False
20260703,50.24,-1.06,42.17,-0.79,40.2,-0.5,0,False,False
20260709,50.83,0.59,42.06,-0.11,40.04,-0.16,1,False,False
20260717,52.42,1.59,43.68,1.62,41.04,1,2,True,True
20260724,53.21,0.79,45.3,1.62,42.41,1.37,3,True,True
20260731,54.28,1.07,45.3,0,42.94,0.53,4,False,True
20260807,56.03,1.75,47.65,2.35,45.63,2.69,5,True,True
20260814,51.96,-4.07,44.03,-3.62,40.65,-4.98,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 5388 | 中磊 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  | no_signal | stale_signal | 1.法律事件之當事人: 原告: 華為技術有限公司 被告: 中磊電子德國子公司Sercomm Deutschland GmbH 2.法律事件之法院名稱或處分機關: 歐洲統一專利法院 3.法律事件之相關文書案號: UPC_CFI_9/2023, UPC_CFI_752/2025 4.事實發生日:115/06/21 5.發生原委(含爭訟標的): 本公司德國子公司Sercomm Deutschland GmbH收到華為公司訴訟書，針對中磊於 德國等地區銷售之部分產品提起專利訴訟。 6.處理過程: 本公司已委任國際專利訴訟專業團隊積極應訴，以維護本公司之最佳利益。 7.對公司財務業務影響及預估影響金額: 本公司於德國地區營收比重甚低，預估對本公司財務、營運影響極為有限。 8.因應措施及改善情形: 本公司專注自主技術研發，對於智慧財產權的投入與保護，向以最嚴格標準，謹慎 處理智慧財產權相關事宜。本公司對該訴訟案件將審慎評估，並委任專業律師妥善 因應，以維護公司最佳權益。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第2款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 5388 | 中磊 | revenue_breakout_low_response | 營收爆發低反應股 | 13 | 45 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.法律事件之當事人: 原告: 華為技術有限公司 被告: 中磊電子德國子公司Sercomm Deutschland GmbH 2.法律事件之法院名稱或處分機關: 歐洲統一專利法院 3.法律事件之相關文書案號: UPC_CFI_9/2023, UPC_CFI_752/2025 4.事實發生日:115/06/21 5.發生原委(含爭訟標的): 本公司德國子公司Sercomm Deutschland GmbH收到華為公司訴訟書，針對中磊於 德國等地區銷售之部分產品提起專利訴訟。 6.處理過程: 本公司已委任國際專利訴訟專業團隊積極應訴，以維護本公司之最佳利益。 7.對公司財務業務影響及預估影響金額: 本公司於德國地區營收比重甚低，預估對本公司財務、營運影響極為有限。 8.因應措施及改善情形: 本公司專注自主技術研發，對於智慧財產權的投入與保護，向以最嚴格標準，謹慎 處理智慧財產權相關事宜。本公司對該訴訟案件將審慎評估，並委任專業律師妥善 因應，以維護公司最佳權益。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第2款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 5388 | 中磊 | 22 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 5388 | 中磊 | 35 | 1 | 853350.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
