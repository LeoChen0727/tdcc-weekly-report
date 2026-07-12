# INDIVIDUAL STOCK CHATGPT PACKET - 3094 聯傑

## Metadata
- generated_at: 2026-07-12 22:26:59 Asia/Taipei
- stock_id: 3094
- stock_name: 聯傑
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3094_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3094_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3094_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3094_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3094_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3094_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3094_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3094_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3094_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3094_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3094_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3094_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3094.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3094.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3094.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3094.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3094_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3094_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3094_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 營收成長股價回檔 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260709
- open: 41.35
- high: 42.1
- low: 40.2
- close: 40.35
- volume: 3057016
- ma5: 40.85
- ema23_primary: 38.61
- distance_to_ema23_pct: 4.5
- ma20: 39.2
- ma60: 33.46
- ma120: 28.9
- return_5d: 1.13
- return_20d: 39.62
- volume_ratio: 0.51
- distance_to_ma20_pct_auxiliary: 2.94
- distance_to_high_60_pct: -12.57

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,29.8,29.8,28.3,29.25,450611,31.65,-7.59,33.33,28.2,0.16
20260612,30.15,32.15,30.1,32.15,1780010,31.69,1.44,33.31,28.34,0.67
20260615,33.1,35.35,33,35.35,4822593,32,10.47,33.39,28.52,1.75
20260616,36.8,37.4,35,36.15,5594275,32.34,11.77,33.48,28.73,1.99
20260617,36.95,39.75,36.95,39,14212332,32.9,18.54,33.62,28.98,4.57
20260618,39,39.55,38,38.25,5046865,33.34,14.71,33.73,29.24,1.66
20260622,40.2,41.8,39,41.8,10181025,34.05,22.76,34.06,29.55,3
20260623,45,45.9,41.1,41.15,10729489,34.64,18.79,34.28,29.85,2.9
20260624,40.5,45.25,40.3,45.25,14669750,35.53,27.37,34.8,30.21,3.41
20260625,46,46.15,42.25,43.3,10709516,36.17,19.7,35.19,30.55,2.31
20260626,42.65,42.65,39.6,39.7,4484386,36.47,8.87,35.46,30.84,0.95
20260629,39.6,41.45,38.35,40.55,3981245,36.81,10.17,35.79,31.14,0.83
20260630,41,41.9,39.3,39.45,6074000,37.03,6.54,36.06,31.42,1.21
20260701,39.55,41.35,38.45,38.45,3569000,37.15,3.51,36.3,31.69,0.7
20260702,38.5,40.4,38.45,39.9,2400000,37.38,6.75,36.66,31.98,0.46
20260703,39.6,40.25,38.85,39,1638734,37.51,3.97,36.97,32.23,0.31
20260706,41.9,42.9,41.5,42.9,4927000,37.96,13.01,37.52,32.56,0.91
20260707,42.95,43.4,39.05,39.5,7138774,38.09,3.71,38.02,32.84,1.25
20260708,39.8,43.2,38.2,42.5,5499791,38.46,10.52,38.62,33.17,0.93
20260709,41.35,42.1,40.2,40.35,3057016,38.61,4.5,39.2,33.46,0.51
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 16.03
- over_600_ratio: 12.51
- over_800_ratio: 12.51
- over_1000_ratio: 11.43
- over_400_change_1w: -2.1
- over_800_change_1w: -2.23
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,16.5,,12.5,,11.42,,0,False,False
20260508,19.63,3.13,14.23,1.73,13.15,1.73,1,True,True
20260515,16.71,-2.92,12.49,-1.74,11.41,-1.74,0,False,False
20260522,17,0.29,13.47,0.98,11.41,0,1,False,True
20260529,17.62,0.62,12.49,-0.98,11.41,0,2,False,False
20260605,16.75,-0.87,12.52,0.03,11.44,0.03,3,False,True
20260612,16.32,-0.43,12.54,0.02,11.46,0.02,4,False,True
20260618,20.74,4.42,13.71,1.17,12.63,1.17,5,True,True
20260626,18.13,-2.61,14.74,1.03,11.43,-1.2,6,False,True
20260703,16.03,-2.1,12.51,-2.23,11.43,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3094 | 聯傑 | revenue_pullback | 營收成長股價回檔 | 77.0 |  |  |  |  |  | continued_overheated | 1.事實發生日:115/06/18 2.發生緣由:依臺灣證券交易所股份有限公司指示辦理。 3.財務業務資訊: 期間　　　　　　　月　　　　　　　　　　　季　　　　　　   最近四季累計 ＝＝＝＝　＝＝＝＝＝＝＝＝＝＝＝　＝＝＝＝＝＝＝＝＝＝＝　＝＝＝＝＝＝＝            最近一月　　與去年　　　最近一季　　與去年　　  114年第二季 科目　　   115年5月 　 同期增減%　 115年第一季 同期增減%　 至115年第一季            (IFRS合併　   　        (IFRS合併　　            (IFRS合併               自結數)                 查核數)                  查核數) 營業收入　　 19.74      16.46%      47.21       -8.50%        183.37 (百萬) 稅前淨利　  　4.87     253.63%       7.48       17.15%         25.92 (百萬) 歸屬母公司 業主淨利　    4.14     303.94%       5.76       24.70%         21.50 (百萬) 每股盈餘　    0.05     350.00%       0.07       16.67%          0.26 (元) 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3094 | 聯傑 | 2 | 1 | 3 | 4 | 13 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
