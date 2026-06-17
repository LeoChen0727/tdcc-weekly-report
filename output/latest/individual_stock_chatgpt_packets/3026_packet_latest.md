# INDIVIDUAL STOCK CHATGPT PACKET - 3026 禾伸堂

## Metadata
- generated_at: 2026-06-17 22:23:32 Asia/Taipei
- stock_id: 3026
- stock_name: 禾伸堂
- packet_status: standard_180d_window_packet
- latest_price_date: 20260617
- price_rows: 283
- latest_tdcc_date: 20260612
- tdcc_rows: 7
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3026_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3026_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3026_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3026_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3026_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3026_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3026_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3026_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3026_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3026_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3026_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3026_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3026.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3026.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3026.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3026.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3026_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3026_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3026_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 歷史不足、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足、股價乖離過大

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
- insufficient_tdcc_history
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260617
- open: 830
- high: 896
- low: 805
- close: 896
- volume: 15854334
- ma5: 802
- ema23_primary: 607.11
- distance_to_ema23_pct: 47.59
- ma20: 611.2
- ma60: 346.32
- ma120: 226.17
- return_5d: 43.13
- return_20d: 174.01
- volume_ratio: 4.13
- distance_to_ma20_pct_auxiliary: 46.6
- distance_to_high_60_pct: -2.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260518,348,359.5,340,359.5,2022392,274.54,30.95,274.15,183.38,0.22
20260519,386,386,360,365,1514422,282.08,29.4,280.7,187.72,0.16
20260520,382,401.5,381,394.5,3249385,291.45,35.36,287.68,192.53,0.35
20260521,428,433.5,427,433.5,2080118,303.28,42.94,296.95,198.02,0.23
20260522,460,476.5,460,476.5,1700070,317.72,49.98,309.6,204.05,0.19
20260525,522,524,522,523,1786878,334.83,56.2,324.95,210.8,0.2
20260526,523,570,471,570,3383416,354.42,60.82,342.55,218.3,0.38
20260527,599,620,596,608,1917131,375.55,61.89,361.25,226.45,0.22
20260528,608,635,585,605,2506943,394.68,53.29,379.7,234.62,0.31
20260529,640,641,615,641,1558340,415.2,54.38,401.12,243.41,0.21
20260601,671,699,665,672,1634588,436.6,53.92,423.43,252.85,0.25
20260602,640,650,605,650,3276908,454.39,43.05,443.5,261.87,0.53
20260603,638,650,628,640,1133009,469.85,36.21,461.85,270.71,0.22
20260604,640,650,605,650,3276908,484.87,34.06,479.35,279.82,0.68
20260605,595,640,562,626,1633575,496.63,26.05,494.15,288.51,0.43
20260611,655,695,590,695,3544235,513.16,35.44,512.42,298.32,1.49
20260612,764,764,764,764,2566138,534.06,43.05,534.12,309.29,1.08
20260615,840,840,840,840,2593202,559.56,50.12,559.88,321.49,1.07
20260616,882,915,785,815,19549082,580.84,40.31,582.75,333.27,6.15
20260617,830,896,805,896,15854334,607.11,47.59,611.2,346.32,4.13
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 56.45
- over_600_ratio: 51.24
- over_800_ratio: 46.29
- over_1000_ratio: 42.52
- over_400_change_1w: 0.23
- over_800_change_1w: 1.6
- over_1000_change_1w: 2.07
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.75,,45.71,,41.38,,0,False,False
20260508,52.93,0.18,42.6,-3.11,39.36,-2.02,1,False,False
20260515,54.28,1.35,44.01,1.41,40.2,0.84,2,True,True
20260522,55.19,0.91,43.28,-0.73,39.46,-0.74,3,False,False
20260529,56.25,1.06,44.6,1.32,40.28,0.82,4,True,True
20260605,56.22,-0.03,44.69,0.09,40.45,0.17,5,False,True
20260612,56.45,0.23,46.29,1.6,42.52,2.07,6,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3026 | 禾伸堂 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_overheated | 1.事實發生日:115/06/16 2.發生緣由:依臺灣證券交易所股份有限公司通知辦理公告 3.財務業務資訊: 期間　　　　　　　(月)                   (季)              (最近四季累計) ＝＝＝＝  ＝＝＝＝＝＝＝＝＝＝＝　＝＝＝＝＝＝＝＝＝＝＝ 　＝＝＝＝＝＝＝ 　　　　　最近一月　  與去年同期　 最近一季　 與去年同期　  (114年第2季至 科目　　　(115年5月)　　增減%　   (115年第1季)　　增減% 　   115年第1季) 　　　　      (合併自結數)  　         (合併核閱數)       (合併查核/核閱數) ＝＝＝＝　＝＝＝＝＝  ＝＝＝＝＝  ＝＝＝＝＝  ＝＝＝＝＝   ＝＝＝＝＝＝＝ 營業收入　  1,291.19 　   21.34%　　3,618.45　     6.36%　　    13,643.30 （百萬） 稅前淨利      201.80     235.56%　    568.65　    94.65%　　     1,467.33 （百萬）　　 歸屬母公司    168.40     207.44%　　  474.58　　  70.41%　　     1,287.79 業主淨利 （百萬） 每股盈餘        1.02     207.44% 　　   2.86　　  70.41%　           7.76 （元） 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告:無。 7.其他應敘明事項:無。；calendar event: ex_dividend on 20260622; status=confirmed; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3026 | 禾伸堂 | 5 | 2 | 5 | 5 | 6 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
