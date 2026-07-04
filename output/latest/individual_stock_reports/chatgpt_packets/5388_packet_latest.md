# INDIVIDUAL STOCK CHATGPT PACKET - 5388 中磊

## Metadata
- generated_at: 2026-07-04 22:27:21 Asia/Taipei
- stock_id: 5388
- stock_name: 中磊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260703
- price_rows: 297
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
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
- decision_score_high
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
- date: 20260703
- open: 80.3
- high: 81.8
- low: 80.2
- close: 81.6
- volume: 1944820
- ma5: 79.98
- ema23_primary: 82.2
- distance_to_ema23_pct: -0.72
- ma20: 82.75
- ma60: 82.79
- ma120: 81.5
- return_5d: 6.53
- return_20d: -8.21
- volume_ratio: 0.58
- distance_to_ma20_pct_auxiliary: -1.4
- distance_to_high_60_pct: -13.65

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260605,89.8,90.8,88.3,89.6,4060003,85.38,4.95,84.84,81.4,0.57
20260608,81.3,84.9,81.3,84.3,4061479,85.29,-1.16,84.69,81.52,0.6
20260609,85,85.3,83.6,84.9,3358943,85.26,-0.42,84.53,81.62,0.51
20260610,85.4,89,83.8,84,4904100,85.15,-1.35,84.76,81.72,0.84
20260611,84.8,87.1,84.3,86.1,4503860,85.23,1.02,85.18,81.84,0.8
20260612,88.6,89.3,85.3,85.3,3598847,85.24,0.08,85.56,81.92,0.65
20260615,87,87,84.8,86.5,2382296,85.34,1.36,86.01,82.04,0.43
20260616,86.5,86.9,84.2,84.2,2477218,85.25,-1.23,86.25,82.12,0.48
20260617,84,85.3,83.6,85.3,2199574,85.25,0.06,86.42,82.22,0.45
20260618,85.7,86,84,84.2,3102958,85.16,-1.13,86.48,82.35,0.64
20260622,84.2,84.3,82.2,82.4,4317474,84.93,-2.98,86.34,82.45,0.9
20260623,83.3,83.7,79.7,79.9,4144148,84.51,-5.46,86.02,82.51,0.87
20260624,79.1,82,79.1,81.7,2253864,84.28,-3.06,85.88,82.62,0.48
20260625,82.4,83.2,80.1,80.2,4066418,83.94,-4.45,85.72,82.65,0.87
20260626,80,80,76.6,76.6,5447718,83.33,-8.07,85.31,82.66,1.17
20260629,76.5,78.2,76.2,77.4,1715271,82.83,-6.56,84.85,82.69,0.38
20260630,78.3,80.8,77.6,80.8,2765000,82.66,-2.25,84.39,82.77,0.67
20260701,81.2,81.2,79,79.6,2562000,82.41,-3.41,83.7,82.76,0.69
20260702,80.2,82,79.8,80.5,3589000,82.25,-2.13,83.12,82.79,1.02
20260703,80.3,81.8,80.2,81.6,1944820,82.2,-0.72,82.75,82.79,0.58
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 50.24
- over_600_ratio: 44.85
- over_800_ratio: 42.17
- over_1000_ratio: 40.2
- over_400_change_1w: -1.06
- over_800_change_1w: -0.79
- over_1000_change_1w: -0.5
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.72,,46.35,,44.02,,0,False,False
20260508,52.38,-1.34,45.37,-0.98,43.63,-0.39,0,False,False
20260515,50.54,-1.84,42.55,-2.82,40.21,-3.42,0,False,False
20260522,51.11,0.57,43.48,0.93,40.89,0.68,1,True,True
20260529,53.66,2.55,45.5,2.02,43.47,2.58,2,True,True
20260605,53.05,-0.61,45.13,-0.37,42.86,-0.61,0,False,False
20260612,53.14,0.09,44.3,-0.83,42.31,-0.55,1,False,False
20260618,52.36,-0.78,43.7,-0.6,42.3,-0.01,0,False,False
20260626,51.3,-1.06,42.96,-0.74,40.7,-1.6,0,False,False
20260703,50.24,-1.06,42.17,-0.79,40.2,-0.5,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 5388 | 中磊 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  | no_signal | stale_signal | 1.法律事件之當事人: 原告: 華為技術有限公司 被告: 中磊電子德國子公司Sercomm Deutschland GmbH 2.法律事件之法院名稱或處分機關: 歐洲統一專利法院 3.法律事件之相關文書案號: UPC_CFI_9/2023, UPC_CFI_752/2025 4.事實發生日:115/06/21 5.發生原委(含爭訟標的): 本公司德國子公司Sercomm Deutschland GmbH收到華為公司訴訟書，針對中磊於 德國等地區銷售之部分產品提起專利訴訟。 6.處理過程: 本公司已委任國際專利訴訟專業團隊積極應訴，以維護本公司之最佳利益。 7.對公司財務業務影響及預估影響金額: 本公司於德國地區營收比重甚低，預估對本公司財務、營運影響極為有限。 8.因應措施及改善情形: 本公司專注自主技術研發，對於智慧財產權的投入與保護，向以最嚴格標準，謹慎 處理智慧財產權相關事宜。本公司對該訴訟案件將審慎評估，並委任專業律師妥善 因應，以維護公司最佳權益。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第2款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260703 | 5388 | 中磊 | revenue_breakout_low_response | 營收爆發低反應股 | 14.0 | 31.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.法律事件之當事人: 原告: 華為技術有限公司 被告: 中磊電子德國子公司Sercomm Deutschland GmbH 2.法律事件之法院名稱或處分機關: 歐洲統一專利法院 3.法律事件之相關文書案號: UPC_CFI_9/2023, UPC_CFI_752/2025 4.事實發生日:115/06/21 5.發生原委(含爭訟標的): 本公司德國子公司Sercomm Deutschland GmbH收到華為公司訴訟書，針對中磊於 德國等地區銷售之部分產品提起專利訴訟。 6.處理過程: 本公司已委任國際專利訴訟專業團隊積極應訴，以維護本公司之最佳利益。 7.對公司財務業務影響及預估影響金額: 本公司於德國地區營收比重甚低，預估對本公司財務、營運影響極為有限。 8.因應措施及改善情形: 本公司專注自主技術研發，對於智慧財產權的投入與保護，向以最嚴格標準，謹慎 處理智慧財產權相關事宜。本公司對該訴訟案件將審慎評估，並委任專業律師妥善 因應，以維護公司最佳權益。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第2款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 5388 | 中磊 | 9 | 5 | 5 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 5388 | 中磊 | 28 | 0 | 983130.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
