# INDIVIDUAL STOCK CHATGPT PACKET - 3090 日電貿

## Metadata
- generated_at: 2026-06-21 22:23:18 Asia/Taipei
- stock_id: 3090
- stock_name: 日電貿
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 286
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3090_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3090_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3090_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3090_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3090.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3090.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3090.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3090.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3090_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3090_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3090_latest.md?ref=main

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
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_confirmed
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
- date: 20260618
- open: 320
- high: 332.5
- low: 316
- close: 332.5
- volume: 23571289
- ma5: 289.5
- ema23_primary: 230.95
- distance_to_ema23_pct: 43.97
- ma20: 239.68
- ma60: 153.79
- ma120: 125.19
- return_5d: 42.7
- return_20d: 69.64
- volume_ratio: 2.04
- distance_to_ma20_pct_auxiliary: 38.73
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,196,215.5,188,215,9230982,136.88,57.07,128.38,107.55,0.53
20260525,229.5,236.5,229.5,236.5,4254466,145.18,62.9,135.39,109.81,0.24
20260526,232.5,233,213,232,8243394,152.42,52.21,142.19,111.97,0.47
20260527,232,241,226,231,2434000,158.97,45.31,148.76,114.16,0.14
20260528,231,233,208.5,208.5,2940019,163.09,27.84,154.26,116.02,0.17
20260529,221.5,229,208,229,2746634,168.59,35.84,160.9,118.27,0.16
20260601,225,251,225,233.5,2078112,174,34.2,167.3,120.67,0.12
20260602,233,233,215,220,2465213,177.83,23.71,172.82,122.79,0.15
20260603,216,220,212.5,214,1671944,180.84,18.33,178.25,124.81,0.1
20260604,210,221,208.5,221,2284892,184.19,19.98,183.5,127.03,0.15
20260605,206,221.5,200,221,1832010,187.26,18.02,188.88,129.19,0.13
20260608,199,210,199,209.5,1681081,189.11,10.78,193.53,131.14,0.12
20260609,212,230,209.5,230,2125056,192.52,19.47,199,133.48,0.16
20260610,238,253,211,212,22645462,194.14,9.2,203.47,135.47,1.69
20260611,220.5,233,204.5,233,26407041,197.38,18.05,208.65,137.78,1.98
20260612,247.5,256,241,256,38888837,202.27,26.57,214.35,140.38,2.68
20260615,273.5,281.5,271,281.5,13979967,208.87,34.77,221.03,143.42,1.05
20260616,286.5,309,274,275,36150880,214.38,28.28,226.65,146.34,2.67
20260617,270,302.5,268.5,302.5,25669966,221.72,36.43,232.85,149.8,1.91
20260618,320,332.5,316,332.5,23571289,230.95,43.97,239.68,153.79,2.04
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 69.35
- over_600_ratio: 66.97
- over_800_ratio: 64.07
- over_1000_ratio: 62.53
- over_400_change_1w: 1
- over_800_change_1w: 0.07
- over_1000_change_1w: 1.01
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,61.74,,56.99,,54.85,,0,False,False
20260508,64.61,2.87,60.48,3.49,59.24,4.39,1,True,True
20260515,61.81,-2.8,57.44,-3.04,55.85,-3.39,0,False,False
20260522,67.08,5.27,63.1,5.66,60.58,4.73,1,True,True
20260529,67.81,0.73,63.46,0.36,61.64,1.06,2,True,True
20260605,67.99,0.18,63.19,-0.27,61.3,-0.34,3,False,False
20260612,68.35,0.36,64,0.81,61.52,0.22,4,False,True
20260618,69.35,1,64.07,0.07,62.53,1.01,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3090 | 日電貿 | true_breakout | 嚴格突破 | 94.0 |  |  | breakout_confirmed |  | no_signal | continued_overheated | 1.事實發生日:115/06/16 2.發生緣由:依台灣證券交易所通知辦理。 3.財務業務資訊: 本公司合併財務資訊： 期 間        最近一月     與去年同期   最近一季     與去年同期   最近四季累計 　　       (2026年5月)     增 減 %  (2026年第1季)    增 減 %    2025年第2季至 　　　　　　　　　　　　　　　　　　　　　　                      2026年第1季 科 目　    (IFRS合併自結數)　　  　　(IFRS合併核閱數)        (IFRS合併核閱數) =======   =============== ======== =============== ======== ================ 營業收入　        1629　     19.96　　     4492      18.34          16424 (百萬) 稅前淨利           179    17800.00　　      617      38.65           1761 (百萬) 歸屬母公司業主淨利  141　   7150.00　　      480      37.14           1383 (百萬) 每股盈餘          0.49　   5000.00　　     1.70       1.80           5.51 (元)  4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:每股盈餘除最近一月及去年同期係依普通股期末股數計算外， 餘係依普通股加權平均股數計算，最近一月(2026年5月)及去年同期(2025年5月) 係分別依287,567仟股及212,597仟股計算；最近一季(2026年第1季)及去年同期 (2025年第1季)係分別依282,583仟股及210,278仟股計算； 最近四季累計(2025年第2季至2026年第1季)係依2025年228,734仟股及 2026年第1季282,583仟股計算之數值相加。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3090 | 日電貿 | 6 | 1 | 5 | 7 | 8 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3090 | 日電貿 | 67 | 0 | 9794570.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
