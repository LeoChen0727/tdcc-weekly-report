# INDIVIDUAL STOCK CHATGPT PACKET - 3372 典範

## Metadata
- generated_at: 2026-06-24 22:23:28 Asia/Taipei
- stock_id: 3372
- stock_name: 典範
- packet_status: standard_180d_window_packet
- latest_price_date: 20260624
- price_rows: 155
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3372_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3372_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3372.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3372.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3372.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3372.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3372_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3372_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3372_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260624
- open: 22.4
- high: 23.7
- low: 22
- close: 23
- volume: 3655000
- ma5: 21.66
- ema23_primary: 20.93
- distance_to_ema23_pct: 9.89
- ma20: 21.14
- ma60: 20.08
- ma120: 20.98
- return_5d: 15.58
- return_20d: 4.31
- volume_ratio: 3.28
- distance_to_ma20_pct_auxiliary: 8.77
- distance_to_high_60_pct: -2.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260527,22.4,22.95,21.45,22.05,22000,20.07,9.88,19.72,20.24,0.04
20260528,22.05,22.3,21,21.5,22000,20.19,6.5,19.89,20.19,0.04
20260529,21.7,22.1,21.5,21.75,22000,20.32,7.05,20.05,20.17,0.04
20260601,22,22.2,21.7,22,22000,20.46,7.54,20.21,20.18,0.04
20260602,22.05,22.4,21.2,22.25,22,20.61,7.97,20.34,20.18,0
20260603,22,22.35,21.85,21.9,22000,20.71,5.72,20.45,20.18,0.05
20260604,21.9,23.7,21.9,22.9,23000,20.9,9.59,20.61,20.23,0.06
20260605,22.5,22.5,20.95,21.2,22000,20.92,1.33,20.68,20.25,0.06
20260608,19.1,19.95,19.1,19.7,1053000,20.82,-5.38,20.68,20.23,2.9
20260609,20.25,20.55,19.9,20.35,525000,20.78,-2.07,20.73,20.22,1.53
20260610,20,20.4,19.3,19.3,1060000,20.66,-6.57,20.75,20.19,2.97
20260611,19.4,19.8,19.1,19.75,652000,20.58,-4.04,20.77,20.17,1.84
20260612,19.9,20.25,19.7,19.7,609000,20.51,-3.94,20.78,20.14,1.79
20260615,20.2,20.9,20.05,20.35,1044000,20.5,-0.71,20.84,20.09,2.88
20260616,20.85,20.85,19.9,19.9,691000,20.45,-2.67,20.89,20.05,1.85
20260617,19.9,20.35,19.75,19.9,1002000,20.4,-2.45,20.93,19.99,2.59
20260618,20.15,20.45,20.1,20.4,994000,20.4,-0,20.96,19.98,2.53
20260622,20.6,21.75,19.75,21.5,2101000,20.49,4.92,21.02,19.99,4.23
20260623,21.9,23.65,21.5,23.5,8758000,20.74,13.29,21.1,20.03,9.38
20260624,22.4,23.7,22,23,3655000,20.93,9.89,21.14,20.08,3.28
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 48.52
- over_600_ratio: 46.59
- over_800_ratio: 45.42
- over_1000_ratio: 43.86
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: -0.12
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.39,,44.44,,43.96,,0,False,False
20260508,46.39,0,44.44,0,43.96,0,0,False,False
20260515,46.88,0.49,44.67,0.23,44.19,0.23,1,True,True
20260522,48.01,1.13,44.67,0,44.19,0,2,False,False
20260529,48.39,0.38,46.42,1.75,44.48,0.29,3,True,True
20260605,49.15,0.76,46.1,-0.32,45.12,0.64,4,False,True
20260612,48.52,-0.63,45.42,-0.68,43.98,-1.14,0,False,False
20260618,48.52,0,45.42,0,43.86,-0.12,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 3372 | 典範 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_overheated | 1.董事會決議或公司決定增資基準日期:115/06/12 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/06/10 4.董事會決議(追補)發行日期:115/03/03 5.發行總金額及股數:總金額600,000,000元；60,000,000股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:每股新台幣16.8元 10.員工認股股數:依公司法第267條規定，保留增資發行股數之10%， 計6,000,000股由本公司員工承購。 11.原股東認購比率:80%計48,000,000股 12.公開銷售方式及股數:依證券交易法第28條之1規定，提撥發行新股總額10% 計6,000,000股對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股得由股東在 停止過戶日起五日內，逕向本公司股務代理機構辦理拼湊，其拼湊不足一股之 畸零股及原股東及員工放棄認購或認購不足及逾期未申報拼湊之部分， 擬授權董事長洽特定人按發行價格認購之。對外公開承銷認購不足部分， 擬依「中華民國證券商業同業公會證券商承銷或再行銷售有價證券處理辦法」 規定辦理。 14.本次發行新股之權利義務:與已發行之原有股份相同。 15.本次增資資金用途:支應資本支出、充實營運資金。 16.現金增資認股基準日:115/07/06 17.最後過戶日:115/07/01 18.停止過戶起始日期:115/07/02 19.停止過戶截止日期:115/07/06 20.股款繳納期間: (1)原股東及員工繳款期間:115/07/09~115/07/15 (2)特定人繳款期間:115/07/16~115/07/20 21.與代收及專戶存儲價款行庫訂約日期:民國115年06月23日 22.委託代收存款機構:臺灣銀行股份有限公司高雄加工出口區分行及全台分行 23.委託存儲款項機構:元大銀行高雄分行 24.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 3372 | 典範 | 3 | 3 | 3 | 3 | 5 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
