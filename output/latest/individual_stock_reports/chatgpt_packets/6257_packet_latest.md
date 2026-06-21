# INDIVIDUAL STOCK CHATGPT PACKET - 6257 矽格

## Metadata
- generated_at: 2026-06-21 22:24:10 Asia/Taipei
- stock_id: 6257
- stock_name: 矽格
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6257_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6257_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6257_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6257_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6257_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6257_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6257_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6257_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6257_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6257_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6257_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6257_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6257.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6257.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6257.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6257.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6257_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6257_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6257_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260618
- open: 216.5
- high: 235
- low: 216.5
- close: 235
- volume: 17090675
- ma5: 221.3
- ema23_primary: 215.77
- distance_to_ema23_pct: 8.91
- ma20: 221.05
- ma60: 195.27
- ma120: 159.86
- return_5d: 14.36
- return_20d: 8.54
- volume_ratio: 1.57
- distance_to_ma20_pct_auxiliary: 6.31
- distance_to_high_60_pct: -2.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,221,235,219.5,222,13548709,200.93,10.49,202.62,167.1,0.88
20260525,225,236,224,231.5,10422000,203.48,13.77,204.95,168.78,0.7
20260526,236,239.5,227,237,14407436,206.27,14.9,207.9,170.44,0.97
20260527,242,242,230.5,233.5,12315942,208.54,11.97,210.55,171.82,0.82
20260528,233.5,240.5,228,229,12607598,210.24,8.92,213.12,173.36,0.82
20260529,234,236.5,224.5,227.5,13335409,211.68,7.47,215.5,174.88,0.86
20260601,230,230,218,219.5,13427032,212.33,3.38,216.95,176.43,0.87
20260602,220.5,227,213.5,215,13068896,212.56,1.15,217.85,177.8,0.88
20260603,220.5,234.5,220,230,15054832,214.01,7.47,219.18,179.45,1.05
20260604,228,237,227,228,11694833,215.18,5.96,219.93,181.28,0.86
20260605,228,228,219,223,8807182,215.83,3.32,220.53,182.91,0.67
20260608,201,205.5,201,201,11533410,214.59,-6.33,219.95,184.07,0.88
20260609,203.5,210.5,200,208.5,8090744,214.08,-2.61,219.88,185.38,0.63
20260610,206,218,203.5,203.5,7985179,213.2,-4.55,219.45,186.59,0.62
20260611,203.5,208,195.5,205.5,5998458,212.56,-3.32,219.2,187.85,0.48
20260612,215,224,214,221.5,9227154,213.31,3.84,219.43,189.33,0.77
20260615,224,227.5,221,222,6718746,214.03,3.72,219.6,190.76,0.58
20260616,224,224.5,214,214,6669072,214.03,-0.01,219.78,192.08,0.6
20260617,212,215.5,209,214,5900621,214.03,-0.01,220.12,193.44,0.55
20260618,216.5,235,216.5,235,17090675,215.77,8.91,221.05,195.27,1.57
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 48.55
- over_600_ratio: 44.62
- over_800_ratio: 40.92
- over_1000_ratio: 39.47
- over_400_change_1w: -0.25
- over_800_change_1w: -0.63
- over_1000_change_1w: -0.28
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,53.32,,47.03,,44.07,,0,False,False
20260508,53.18,-0.14,46.32,-0.71,44.11,0.04,1,False,True
20260515,51.59,-1.59,45.03,-1.29,42.1,-2.01,0,False,False
20260522,52.48,0.89,45.66,0.63,42.97,0.87,1,True,True
20260529,52.33,-0.15,45.45,-0.21,42.35,-0.62,0,False,False
20260605,50.77,-1.56,43.16,-2.29,40.78,-1.57,0,False,False
20260612,48.8,-1.97,41.55,-1.61,39.75,-1.03,0,False,False
20260618,48.55,-0.25,40.92,-0.63,39.47,-0.28,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 6257 | 矽格 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_put_bullish | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/06/23 1.召開法人說明會之日期：115/06/23 2.召開法人說明會之時間：14 時 30 分  3.召開法人說明會之地點：線上法人說明會-Webex 4.法人說明會擇要訊息：本公司受邀參加凱基證券舉辦之線上法說會 5.其他應敘明事項：會後將於公開資訊觀測站公告相關資訊 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 6257 | 矽格 | 12 | 1 | 5 | 10 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 6257 | 矽格 | 116 | 8 | 8950370.0 | 61700.0 | 145.06 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
