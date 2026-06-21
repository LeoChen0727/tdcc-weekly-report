# INDIVIDUAL STOCK CHATGPT PACKET - 3094 聯傑

## Metadata
- generated_at: 2026-06-21 22:23:18 Asia/Taipei
- stock_id: 3094
- stock_name: 聯傑
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
- date: 20260618
- open: 39
- high: 39.55
- low: 38
- close: 38.25
- volume: 5046865
- ma5: 36.18
- ema23_primary: 33.34
- distance_to_ema23_pct: 14.71
- ma20: 33.73
- ma60: 29.24
- ma120: 26.92
- return_5d: 30.77
- return_20d: 6.4
- volume_ratio: 1.66
- distance_to_ma20_pct_auxiliary: 13.38
- distance_to_high_60_pct: -3.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,35.95,36.6,35.2,35.35,3206109,30.92,14.31,30.79,26.14,0.82
20260525,35.7,37,35.7,36.6,4570406,31.4,16.57,31.26,26.32,1.14
20260526,37,37,34.5,34.95,2762556,31.69,10.28,31.7,26.49,0.67
20260527,34.95,36.4,34.9,35.55,4056399,32.01,11.05,32.18,26.66,0.95
20260528,35.6,36.3,33.7,34.25,2950743,32.2,6.37,32.58,26.81,0.67
20260529,35,35,33.6,33.95,1641857,32.35,4.96,32.97,26.96,0.37
20260601,33.7,34.55,33.4,34,1803792,32.48,4.67,33.27,27.14,0.42
20260602,34.3,35.5,32.7,33.75,1724141,32.59,3.56,33.58,27.31,0.39
20260603,33.5,33.6,32.6,32.7,1506207,32.6,0.31,33.7,27.46,0.37
20260604,32.7,33.1,32.4,32.7,928672,32.61,0.28,33.66,27.63,0.25
20260605,32.9,33.25,31.65,31.85,1029382,32.54,-2.13,33.71,27.79,0.31
20260608,28.9,29.75,28.8,29.55,878734,32.29,-8.5,33.64,27.89,0.27
20260609,30.15,31,28.95,30.45,1017000,32.14,-5.26,33.59,28.01,0.32
20260610,30.1,30.8,28.85,28.9,894221,31.87,-9.32,33.51,28.11,0.29
20260611,29.8,29.8,28.3,29.25,450611,31.65,-7.59,33.33,28.2,0.16
20260612,30.15,32.15,30.1,32.15,1780010,31.69,1.44,33.31,28.34,0.67
20260615,33.1,35.35,33,35.35,4822593,32,10.47,33.39,28.52,1.75
20260616,36.8,37.4,35,36.15,5594275,32.34,11.77,33.48,28.73,1.99
20260617,36.95,39.75,36.95,39,14212332,32.9,18.54,33.62,28.98,4.57
20260618,39,39.55,38,38.25,5046865,33.34,14.71,33.73,29.24,1.66
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 20.74
- over_600_ratio: 16.03
- over_800_ratio: 13.71
- over_1000_ratio: 12.63
- over_400_change_1w: 4.42
- over_800_change_1w: 1.17
- over_1000_change_1w: 1.17
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

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
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3094 | 聯傑 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | repeated_but_no_breakout | 1.事實發生日:115/06/18 2.發生緣由:依臺灣證券交易所股份有限公司指示辦理。 3.財務業務資訊: 期間　　　　　　　月　　　　　　　　　　　季　　　　　　   最近四季累計 ＝＝＝＝　＝＝＝＝＝＝＝＝＝＝＝　＝＝＝＝＝＝＝＝＝＝＝　＝＝＝＝＝＝＝            最近一月　　與去年　　　最近一季　　與去年　　  114年第二季 科目　　   115年5月 　 同期增減%　 115年第一季 同期增減%　 至115年第一季            (IFRS合併　   　        (IFRS合併　　            (IFRS合併               自結數)                 查核數)                  查核數) 營業收入　　 19.74      16.46%      47.21       -8.50%        183.37 (百萬) 稅前淨利　  　4.87     253.63%       7.48       17.15%         25.92 (百萬) 歸屬母公司 業主淨利　    4.14     303.94%       5.76       24.70%         21.50 (百萬) 每股盈餘　    0.05     350.00%       0.07       16.67%          0.26 (元) 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無。；calendar event: ex_dividend on 20260622; status=confirmed; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3094 | 聯傑 | 5 | 1 | 5 | 8 | 12 | repeated_but_no_breakout | 近 10 日上榜 8 次、近 20 日上榜 12 次，但尚未有效突破，需等待攻擊確認。 |

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
