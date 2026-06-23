# INDIVIDUAL STOCK CHATGPT PACKET - 8096 擎亞

## Metadata
- generated_at: 2026-06-23 22:24:56 Asia/Taipei
- stock_id: 8096
- stock_name: 擎亞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260622
- price_rows: 153
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8096_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8096_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8096_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8096_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8096_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8096_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8096_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8096_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8096_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8096_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8096_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8096_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8096.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8096.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8096.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8096.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8096_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8096_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8096_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
- entry_style: no_entry_now
- position_sizing: observe_only

### management_plan
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260622
- open: 161
- high: 162
- low: 154
- close: 157.5
- volume: 12759000
- ma5: 150.2
- ema23_primary: 130.36
- distance_to_ema23_pct: 20.82
- ma20: 132.43
- ma60: 107.81
- ma120: 85.28
- return_5d: 18.87
- return_20d: 32.91
- volume_ratio: 2.1
- distance_to_ma20_pct_auxiliary: 18.94
- distance_to_high_60_pct: -2.78

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260525,121,126.5,117.5,124.5,122000,101.4,22.78,99.7,89.53,0.01
20260526,124.5,125,117,119.5,120000,102.91,16.12,101.09,90.28,0.01
20260527,123,125,117.5,121,120000,104.42,15.88,102.58,91.1,0.01
20260528,121.5,129,120,121,124000,105.8,14.37,104.03,91.94,0.01
20260529,124.5,127.5,118.5,122.5,123000,107.19,14.28,105.69,92.89,0.01
20260601,124,134.5,123.5,134.5,130000,109.47,22.87,107.75,94.11,0.01
20260602,137,145,132,137,137,111.76,22.58,109.79,95.34,0
20260603,136.5,140,134.5,136.5,137000,113.82,19.92,111.78,96.58,0.01
20260604,134,142,134,136,138000,115.67,17.57,113.78,97.78,0.01
20260605,131.5,137.5,122.5,128.5,129000,116.74,10.07,115.42,98.74,0.01
20260608,116,121.5,116,119.5,11546000,116.97,2.16,116.47,99.48,1.24
20260609,122,130,121,125.5,14114000,117.68,6.64,117.91,100.35,1.54
20260610,124,131,117.5,118,8997000,117.71,0.25,119.08,101.05,0.98
20260611,120,128,117,121,10703000,117.98,2.56,120.27,101.68,1.21
20260612,127,133,126,132.5,12488000,119.19,11.16,122.1,102.54,1.4
20260615,137,145.5,133.5,145.5,11406000,121.38,19.87,124.12,103.48,1.47
20260616,147,150,142,142.5,15495000,123.14,15.72,125.97,104.42,2.37
20260617,144.5,152.5,141.5,150,13118000,125.38,19.63,128.1,105.47,2.17
20260618,150,156.5,147.5,155.5,9641000,127.89,21.59,130.47,106.61,1.77
20260622,161,162,154,157.5,12759000,130.36,20.82,132.43,107.81,2.1
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 58.09
- over_600_ratio: 56.57
- over_800_ratio: 54.69
- over_1000_ratio: 52.84
- over_400_change_1w: 4.28
- over_800_change_1w: 5.34
- over_1000_change_1w: 4.65
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.76,,43.73,,42.48,,0,False,False
20260508,46.84,-0.92,43.6,-0.13,40.47,-2.01,0,False,False
20260515,46.23,-0.61,43.05,-0.55,41.87,1.4,1,False,True
20260522,50.03,3.8,47.16,4.11,45.32,3.45,2,True,True
20260529,53.61,3.58,49.59,2.43,47.8,2.48,3,True,True
20260605,54.01,0.4,50.99,1.4,49.22,1.42,4,True,True
20260612,53.81,-0.2,49.35,-1.64,48.19,-1.03,0,False,False
20260618,58.09,4.28,54.69,5.34,52.84,4.65,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260622 | 8096 | 擎亞 | true_breakout | 嚴格突破 | 84.0 |  |  | platform_breakout |  |  | continued_overheated | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: (1)最近一個月單月資訊： --------------------------------------------------------------------------- 項目/月份                    115年5月      114年5月      與去年同期增減% --------------------------------------------------------------------------- 營業收入(百萬元)              3,981          1,564             155% 稅前淨利(百萬元)               (30)            (8)         持續虧損 歸屬母公司業主淨利(百萬元)        24           (10)           虧轉盈 每股盈餘(元)                   0.16         (0.07)           虧轉盈 --------------------------------------------------------------------------- (2)最近一季單季資訊： --------------------------------------------------------------------------- 項目/月份                   115年第1季   114年第1季      與去年同期增減% --------------------------------------------------------------------------- 營業收入(百萬元)              10,173         14,527            -30% 稅前淨利(百萬元)                 332            237             40% 歸屬母公司業主淨利(百萬元)        284            162             76% 每股盈餘(元)                    1.90           1.08             76% ---------------------------------------------------------------------------- (3)最近四季累計： --------------------------------------------------------------------------- 項目/月份                      114年第2季~115年第1季 --------------------------------------------------------------------------- 營業收入(百萬元)                     30,342 稅前淨利(百萬元)                        301 歸屬母公司業主淨利(百萬元)               255 每股盈餘(元)                           1.71 -------------------------------------------------------------------------- 公司每股面額10元 -------------------------------------------------------------------------- 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之 合併自結數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，係經會計師查核(閱)。 (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經 會計師查核(閱)。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260622 | 8096 | 擎亞 | 2 | 2 | 2 | 3 | 11 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
