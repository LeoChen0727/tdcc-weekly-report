# INDIVIDUAL STOCK CHATGPT PACKET - 8043 蜜望實

## Metadata
- generated_at: 2026-07-15 22:27:50 Asia/Taipei
- stock_id: 8043
- stock_name: 蜜望實
- packet_status: standard_180d_window_packet
- latest_price_date: 20260715
- price_rows: 169
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8043_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8043_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8043.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8043.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8043.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8043.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8043_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8043_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8043_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: high
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
- date: 20260715
- open: 157
- high: 159
- low: 148
- close: 154.5
- volume: 7096000
- ma5: 165
- ema23_primary: 178.07
- distance_to_ema23_pct: -13.24
- ma20: 191.97
- ma60: 145.75
- ma120: 111.93
- return_5d: -13.93
- return_20d: -23.7
- volume_ratio: 0.42
- distance_to_ma20_pct_auxiliary: -19.52
- distance_to_high_60_pct: -35.49

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260616,207.5,222.5,207,211,42122000,157.84,33.68,157.22,108.92,2.98
20260617,208,225,205,220,36332000,163.02,34.95,162.5,111.37,2.57
20260618,219,239.5,218.5,226.5,34165000,168.31,34.57,167.55,113.94,2.36
20260622,228.5,235,212,213,26213000,172.04,23.81,171.68,116.31,1.66
20260623,207,211.5,201,202,11121000,174.53,15.74,175.38,118.47,0.68
20260624,200,206,194,200,10777000,176.66,13.21,179.32,120.61,0.64
20260625,203.5,208,198,199,12161000,178.52,11.47,182.68,122.74,0.7
20260626,197,203.5,183,184.5,8093000,179.02,3.06,185.47,124.63,0.45
20260629,182,183,171,176.5,8166000,178.81,-1.29,187.25,126.42,0.45
20260630,182,194,179,194,5743000,180.07,7.73,189.2,128.51,0.31
20260701,201,213,201,213,20141000,182.82,16.51,192,131,1.03
20260702,208,221.5,194.5,197,33027000,184,7.07,194.3,133.22,1.56
20260703,197,216,191,202.5,25737000,185.54,9.14,197.18,135.49,1.15
20260706,203,209.5,190.5,196,12271000,186.41,5.14,199,137.63,0.53
20260707,196,202,176.5,179.5,10317000,185.84,-3.41,199.22,139.38,0.5
20260708,182.5,182.5,170,179,9635000,185.27,-3.38,198.55,141,0.46
20260709,182,184,173,173,7979000,184.24,-6.1,197.25,142.47,0.4
20260713,174.5,175,160.5,165,8607000,182.64,-9.66,195.93,143.79,0.47
20260714,161.5,167,149.5,153.5,6811000,180.21,-14.82,194.38,144.78,0.4
20260715,157,159,148,154.5,7096000,178.07,-13.24,191.97,145.75,0.42
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 47.55
- over_600_ratio: 45.98
- over_800_ratio: 44.26
- over_1000_ratio: 43.2
- over_400_change_1w: -1.99
- over_800_change_1w: -2.66
- over_1000_change_1w: -3.72
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.18,,58.52,,58.52,,0,False,False
20260508,60.16,-0.02,57.91,-0.61,57.91,-0.61,0,False,False
20260515,60.27,0.11,54.73,-3.18,54.73,-3.18,1,False,False
20260522,64.25,3.98,58.71,3.98,57.63,2.9,2,True,True
20260529,57.39,-6.86,51.96,-6.75,51.96,-5.67,0,False,False
20260605,59.02,1.63,56.31,4.35,55.28,3.32,1,True,True
20260612,61.17,2.15,54.42,-1.89,53.18,-2.1,2,False,False
20260618,60.08,-1.09,53.28,-1.14,53.28,0.1,3,False,True
20260626,49.54,-10.54,46.92,-6.36,46.92,-6.36,0,False,False
20260703,47.55,-1.99,44.26,-2.66,43.2,-3.72,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 8043 | 蜜望實 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理公告。 3.財務業務資訊: (1)單月                          最近一月單月       去年同月      與去年同期增減% 期間                          (115/05)      (114/05) -------------------------------------------------------------------------- 營業收入(百萬元)                 616          386               59.59% 稅前淨利(百萬元)                  -1          -23               95.65% 歸屬母公司業主淨利(百萬元)        -1          -15               93.33% 每股盈餘(元)                   -0.01        -0.19               94.74%  (2)單季                          最近一季單季        去年同期      與去年同期增減% 期間                        (115第1季)      (114第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                1,903         1,053             80.72% 稅前淨利(百萬元)                  134           -17            888.24% 歸屬母公司業主淨利(百萬元)        108           -25            532.00% 每股盈餘(元)                     1.35         -0.31            535.48% (3)最近四季累計 期間                       (114年第2季至115年第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                6,276 稅前淨利(百萬元)                  293 歸屬母公司業主淨利(百萬元)        266 每股盈餘(元)                     3.33 -------------------------------------------------------------------------- 公司每股面額10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:有 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年05月及去年同期比較數之財務資料係本公司 依IFRS會計準則編製之合併自結數，未經會計師查核(核閱)， 僅供投資人參考。 (2)最近一季115年第1季及去年同期比較數係指單季數字， 係本公司依IFRS下編製之合併數，業係經會計師核閱，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季由本公司依IFRS編製之 合併數業經會計師查核(核閱)，僅供投資人參考#欄位說明；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 8043 | 蜜望實 | 14 | 14 | 5 | 10 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
