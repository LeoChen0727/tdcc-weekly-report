# INDIVIDUAL STOCK CHATGPT PACKET - 6213 聯茂

## Metadata
- generated_at: 2026-07-06 22:27:48 Asia/Taipei
- stock_id: 6213
- stock_name: 聯茂
- packet_status: standard_180d_window_packet
- latest_price_date: 20260706
- price_rows: 298
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6213_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6213_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6213_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6213_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6213_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6213_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6213_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6213_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6213_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6213_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6213_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6213_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6213.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6213.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6213.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6213.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6213_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6213_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6213_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前以風險管理為主，不適合新買第一筆。
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
- date: 20260706
- open: 409.5
- high: 411
- low: 379
- close: 396
- volume: 33277000
- ma5: 375.8
- ema23_primary: 318.97
- distance_to_ema23_pct: 24.15
- ma20: 306.55
- ma60: 279
- ma120: 205.1
- return_5d: 15.12
- return_20d: 55.6
- volume_ratio: 1.69
- distance_to_ma20_pct_auxiliary: 29.18
- distance_to_high_60_pct: -3.65

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260608,229.5,244.5,229.5,243.5,7487353,261.83,-7,262.73,230.18,0.46
20260609,249,259,242,257,9522888,261.43,-1.69,261.3,232.26,0.63
20260610,250,272,249.5,254,15359092,260.81,-2.61,260.32,234.2,1.01
20260611,252.5,260,236.5,248,10874563,259.74,-4.52,259.32,236,0.73
20260612,260,263.5,249.5,252.5,9064998,259.14,-2.56,259.3,237.64,0.61
20260615,259.5,269,259,263.5,7633970,259.5,1.54,260.23,239.53,0.52
20260616,267,270.5,255,258,7694528,259.38,-0.53,261.1,241.3,0.53
20260617,255,272.5,253,267.5,10448303,260.05,2.86,262.65,243.37,0.71
20260618,274,290,272.5,280,22287192,261.72,6.99,264.32,245.77,1.45
20260622,293,308,292,308,36208426,265.57,15.98,266.62,248.69,2.18
20260623,304,312,281,281,28641888,266.86,5.3,267.32,250.95,1.66
20260624,309,309,303,309,25462125,270.37,14.29,269.05,253.7,1.46
20260625,329,339.5,329,339.5,26733662,276.13,22.95,272.2,256.73,1.5
20260626,353,373,345,346.5,35982616,282,22.87,276.48,259.98,2
20260629,359.5,359.5,335,344,17126748,287.16,19.79,280.25,263.24,0.96
20260630,357.5,376,353,370.5,18700000,294.11,25.97,284.02,266.7,1.09
20260701,379,384,348.5,360,19536000,299.6,20.16,288.38,269.87,1.16
20260702,357,379.5,353,358.5,20785000,304.51,17.73,292.8,272.73,1.21
20260703,348,394,334,394,30576891,311.96,26.3,299.48,276.01,1.66
20260706,409.5,411,379,396,33277000,318.97,24.15,306.55,279,1.69
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 65.3
- over_600_ratio: 63.83
- over_800_ratio: 61.36
- over_1000_ratio: 58.8
- over_400_change_1w: -0.02
- over_800_change_1w: 0.51
- over_1000_change_1w: -0.29
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.18,,56.01,,54.09,,0,False,False
20260508,60.37,0.19,56.36,0.35,54.89,0.8,1,True,True
20260515,56.44,-3.93,52.9,-3.46,50.86,-4.03,0,False,False
20260522,56.87,0.43,51.93,-0.97,51.16,0.3,1,False,True
20260529,56.49,-0.38,52.51,0.58,50.76,-0.4,2,False,True
20260605,56.62,0.13,52.59,0.08,51.35,0.59,3,True,True
20260612,56.26,-0.36,52.45,-0.14,50.68,-0.67,4,False,False
20260618,57.63,1.37,53.34,0.89,51.09,0.41,5,True,True
20260626,65.32,7.69,60.85,7.51,59.09,8,6,True,True
20260703,65.3,-0.02,61.36,0.51,58.8,-0.29,7,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 6213 | 聯茂 | true_breakout | 嚴格突破 | 77.0 |  |  | platform_breakout |  | no_signal | continued_overheated | 1.事實發生日:115/06/23 2.發生緣由:依臺灣證券交易所股份有限公司通知辦理公告 3.財務業務資訊:  一、本公司合併財務資訊：  科目　　 最近一月　　 與去年同期　　最近一季　　 與去年同期　最近四季累計  期間　　 115年05月　　增　　 減%　 115年第1季 　 增　　 減%　114年第2季至                                                               115年第1季              (自結數)               　(查核數)               (核閱或查核數)  ＝＝＝＝　 ＝＝＝＝　＝＝＝＝＝＝　＝＝＝＝＝＝ ＝＝＝＝＝＝ ＝＝＝＝＝＝＝  營業收入　　 3,803 　      29.31%　  　9,143 　　   20.62%　      34,661  (百萬)  稅前淨利       655        235.90%　      483　      -9.72%　　     2,315  (百萬)  本期淨利       438        265.00%　　    315　      -6.53%　　     1,488  (百萬)  每股盈餘　    1.21        266.67% 　    0.87　      -6.45%　        4.10  (元) 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告:無 7.其他應敘明事項:無；calendar event: ex_dividend on 20260702; status=confirmed; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 6213 | 聯茂 | 2 | 2 | 3 | 7 | 17 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 6213 | 聯茂 | 139 | 8 | 47085610.0 | 509020.0 | 92.5 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
