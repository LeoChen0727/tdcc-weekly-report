# INDIVIDUAL STOCK CHATGPT PACKET - 3231 緯創

## Metadata
- generated_at: 2026-07-15 22:26:56 Asia/Taipei
- stock_id: 3231
- stock_name: 緯創
- packet_status: standard_180d_window_packet
- latest_price_date: 20260715
- price_rows: 304
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3231_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3231_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3231_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3231_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3231_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3231_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3231_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3231_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3231_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3231_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3231_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3231_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3231.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3231.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3231.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3231.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3231_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3231_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3231_latest.md?ref=main

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
- date: 20260715
- open: 144
- high: 146.5
- low: 142.5
- close: 145.5
- volume: 26071700
- ma5: 144.5
- ema23_primary: 153.11
- distance_to_ema23_pct: -4.97
- ma20: 154.97
- ma60: 151.28
- ma120: 141.79
- return_5d: -6.43
- return_20d: -9.91
- volume_ratio: 0.75
- distance_to_ma20_pct_auxiliary: -6.11
- distance_to_high_60_pct: -27.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260616,162,162,158,158,31462271,157.26,0.47,159.05,143.31,0.41
20260617,158.5,164.5,158,162.5,49733205,157.7,3.04,160.55,143.85,0.63
20260618,162,163.5,160.5,161.5,45633029,158.02,2.21,161.62,144.45,0.58
20260622,164.5,166,161.5,162.5,45905638,158.39,2.6,162.53,145.01,0.59
20260623,163,163.5,158,158.5,46744847,158.4,0.06,163,145.52,0.61
20260624,156.5,159.5,155,157.5,30028729,158.32,-0.52,163.57,146.03,0.4
20260625,159.5,162,156.5,160,42348647,158.46,0.97,164.32,146.57,0.56
20260626,159,159,153,153,43076438,158.01,-3.17,164.75,147.03,0.57
20260629,154,158,153.5,154.5,27017688,157.72,-2.04,164.55,147.57,0.38
20260630,157.5,160,156,158.5,27371856,157.78,0.46,163.78,148.09,0.4
20260701,161,162,159,159.5,37036945,157.92,1,162.2,148.67,0.66
20260702,157,160,156,158.5,17411425,157.97,0.33,160.43,149.25,0.36
20260703,157.5,161.5,157.5,159,24768914,158.06,0.6,159.57,149.72,0.57
20260706,161,162,157.5,158,26189698,158.05,-0.03,158.93,150.14,0.64
20260707,158.5,159.5,155.5,155.5,34773345,157.84,-1.48,158.53,150.48,0.9
20260708,150,152,145,146.5,59256833,156.9,-6.63,157.57,150.68,1.54
20260709,147,148,144.5,144.5,29080046,155.86,-7.29,156.9,150.82,0.77
20260713,147,148,142.5,143.5,27031128,154.83,-7.32,156.45,150.99,0.74
20260714,144,145,139,142.5,27925626,153.8,-7.35,155.78,151.13,0.78
20260715,144,146.5,142.5,145.5,26071700,153.11,-4.97,154.97,151.28,0.75
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 62.81
- over_600_ratio: 60.86
- over_800_ratio: 59.63
- over_1000_ratio: 58.54
- over_400_change_1w: -0.39
- over_800_change_1w: -0.33
- over_1000_change_1w: -0.29
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61,,57.62,,56.65,,0,False,False
20260508,62.27,1.27,58.93,1.31,57.91,1.26,1,True,True
20260515,60.85,-1.42,57.61,-1.32,56.52,-1.39,0,False,False
20260522,61.11,0.26,57.73,0.12,56.7,0.18,1,True,True
20260529,62.57,1.46,59.29,1.56,58.18,1.48,2,True,True
20260605,66.02,3.45,62.74,3.45,61.68,3.5,3,True,True
20260612,64.88,-1.14,61.69,-1.05,60.64,-1.04,0,False,False
20260618,64.37,-0.51,61.14,-0.55,60.08,-0.56,0,False,False
20260626,63.2,-1.17,59.96,-1.18,58.83,-1.25,0,False,False
20260703,62.81,-0.39,59.63,-0.33,58.54,-0.29,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 3231 | 緯創 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  | call_inflow | stale_signal | 1. 原公告日期： 115/06/26 2. 簡述原公告申報內容： 子公司Wistron InfoComm (Vietnam) Co., Ltd(WVN)原於2026年6月26日公告 於金榜工業區以租地委建方式於總金額約為美金138,768仟元預算內興建廠房、倉庫 等配套建物 3. 變動緣由及主要內容： WVN現與非關係人建興越南建設發展責任有限公司簽訂土建工程合約，總金額為 越南盾1兆7,718億元 4. 變動後對公司財務業務之影響： 無 5. 其他應敘明事項： 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260715 | 3231 | 緯創 | revenue_breakout_low_response | 營收爆發低反應股 | 11.0 | 40.0 | D_降級_TDCC轉弱 |  |  | call_inflow | stale_signal | 1. 原公告日期： 115/06/26 2. 簡述原公告申報內容： 子公司Wistron InfoComm (Vietnam) Co., Ltd(WVN)原於2026年6月26日公告 於金榜工業區以租地委建方式於總金額約為美金138,768仟元預算內興建廠房、倉庫 等配套建物 3. 變動緣由及主要內容： WVN現與非關係人建興越南建設發展責任有限公司簽訂土建工程合約，總金額為 越南盾1兆7,718億元 4. 變動後對公司財務業務之影響： 無 5. 其他應敘明事項： 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 3231 | 緯創 | 33 | 9 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 3231 | 緯創 | 206 | 15 | 11489920.0 | 69370.0 | 165.63 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
