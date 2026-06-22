# INDIVIDUAL STOCK CHATGPT PACKET - 2838 聯邦銀

## Metadata
- generated_at: 2026-06-22 22:23:11 Asia/Taipei
- stock_id: 2838
- stock_name: 聯邦銀
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2838_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2838_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2838_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2838_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2838_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2838_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2838_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2838_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2838_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2838_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2838_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2838_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2838.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2838.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2838.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2838.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2838_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2838_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2838_latest.md?ref=main

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
- date: 20260618
- open: 22.6
- high: 22.8
- low: 22.35
- close: 22.75
- volume: 7573267
- ma5: 22.18
- ema23_primary: 21.34
- distance_to_ema23_pct: 6.63
- ma20: 21.18
- ma60: 20.75
- ma120: 20.04
- return_5d: 5.08
- return_20d: 13.18
- volume_ratio: 3
- distance_to_ma20_pct_auxiliary: 7.44
- distance_to_high_60_pct: -0.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,20.1,20.3,20.1,20.15,1277843,20.33,-0.89,20.29,20.34,0.8
20260525,20.15,20.15,20,20.1,1511842,20.31,-1.04,20.29,20.34,0.94
20260526,20.05,20.25,20.05,20.25,1151599,20.31,-0.28,20.3,20.35,0.72
20260527,20.25,20.5,20.1,20.5,1664653,20.32,0.88,20.32,20.35,1.03
20260528,20.5,20.5,20.15,20.2,1301339,20.31,-0.55,20.32,20.35,0.81
20260529,20.2,20.45,20.15,20.45,2471423,20.32,0.62,20.34,20.36,1.51
20260601,20.4,20.5,20.05,20.5,2440712,20.34,0.8,20.36,20.38,1.49
20260602,20.45,20.75,20.3,20.6,1881136,20.36,1.18,20.36,20.39,1.13
20260603,20.6,21.4,20.45,21.1,3245589,20.42,3.32,20.39,20.42,1.87
20260604,21.1,21.45,21.1,21.35,2416193,20.5,4.15,20.43,20.45,1.35
20260605,21.3,21.6,21,21.55,2439982,20.59,4.68,20.48,20.48,1.34
20260608,20.95,21.3,20.75,20.75,2506121,20.6,0.73,20.48,20.49,1.35
20260609,20.6,21.9,20.6,21.8,3947529,20.7,5.31,20.54,20.52,2
20260610,21.7,21.85,21.5,21.65,1801666,20.78,4.19,20.6,20.55,0.91
20260611,21.75,21.85,21.3,21.65,2036323,20.85,3.83,20.68,20.57,1.03
20260612,21.7,22,21.6,21.75,1666969,20.93,3.93,20.76,20.6,0.84
20260615,22,22.1,21.75,21.9,3872062,21.01,4.25,20.84,20.63,1.84
20260616,21.9,22.3,21.8,22.05,2315772,21.09,4.53,20.92,20.66,1.08
20260617,22.1,22.55,22,22.45,2893588,21.21,5.86,21.04,20.7,1.33
20260618,22.6,22.8,22.35,22.75,7573267,21.34,6.63,21.18,20.75,3
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 90.8
- over_600_ratio: 90.03
- over_800_ratio: 89.62
- over_1000_ratio: 89.12
- over_400_change_1w: 0.07
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,90.7,,89.57,,89.18,,0,False,False
20260508,90.72,0.02,89.59,0.02,89.15,-0.03,1,False,True
20260515,90.67,-0.05,89.56,-0.03,89.08,-0.07,0,False,False
20260522,90.61,-0.06,89.52,-0.04,89.02,-0.06,0,False,False
20260529,90.61,0,89.46,-0.06,89.03,0.01,1,False,True
20260605,90.7,0.09,89.55,0.09,89.07,0.04,2,True,True
20260612,90.73,0.03,89.58,0.03,89.08,0.01,3,True,True
20260618,90.8,0.07,89.62,0.04,89.12,0.04,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2838 | 聯邦銀 | true_breakout | 嚴格突破 | 148.0 |  |  | breakout_confirmed |  |  | continued_many_days | 1.董事會、股東會決議或公司決定日期:115/06/17 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放特別股股利種類及金額: 本次盈餘分派配發之特別股現金股利526,125,000元，每股配發2.630625元 （係按112年4月24日重設利率5.26125%核算），按配息基準日本行特別股股東 名冊記載之各股東持有股份比例計算分配至元為止，未滿1元之款項，列入公司之其他 收入。 4.除權（息）交易日:115/07/03 5.最後過戶日:115/07/06 6.停止過戶起始日期:115/07/07 7.停止過戶截止日期:115/07/11 8.除權（息）基準日:115/07/11 9.特別股最後申請轉換日期:NA 10.特別股停止轉換起始日期:NA 11.特別股停止轉換截止日期:NA 12.特別股現金股利發放日期:115/07/27 13.其他應敘明事項:如因受不可抗力因素，政府公布放假，股利發放日將順延至下一個 營業日。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2838 | 聯邦銀 | 17 | 1 | 5 | 10 | 17 | continued_many_days | 連續 17 日上榜，需區分醞釀延續或訊號鈍化。 |

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
