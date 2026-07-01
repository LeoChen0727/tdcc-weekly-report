# INDIVIDUAL STOCK CHATGPT PACKET - 8358 金居

## Metadata
- generated_at: 2026-07-01 22:29:00 Asia/Taipei
- stock_id: 8358
- stock_name: 金居
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 160
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8358_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8358_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8358_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8358_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8358_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8358_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8358_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8358_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8358_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8358_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8358_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8358_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8358.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8358.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8358.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8358.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8358_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8358_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8358_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260701
- open: 626
- high: 639
- low: 580
- close: 587
- volume: 12352000
- ma5: 586.6
- ema23_primary: 589.9
- distance_to_ema23_pct: -0.49
- ma20: 607.8
- ma60: 484.77
- ma120: 372.07
- return_5d: -7.99
- return_20d: -6.38
- volume_ratio: 1.89
- distance_to_ma20_pct_auxiliary: -3.42
- distance_to_high_60_pct: -22.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,635,654,606,615,623000,509.15,20.79,509.05,368.34,0.06
20260604,608,626,565,565,602000,513.8,9.96,513.85,373.88,0.07
20260605,543,596,515,596,556000,520.65,14.47,520.92,380.07,0.08
20260608,537,590,537,586,2658000,526.1,11.39,527.12,386.07,0.51
20260609,586,613,560,610,1992000,533.09,14.43,533.77,392.43,0.49
20260610,596,605,555,555,1797000,534.91,3.75,538.73,397.65,0.57
20260611,555,564,510,540,3154000,535.34,0.87,544.38,402.48,1.77
20260612,579,584,562,574,1869000,538.56,6.58,553.6,407.67,1.08
20260615,594,625,594,624,1740000,545.68,14.35,563.4,413.51,1.05
20260616,625,638,615,632,2191000,552.87,14.31,573.55,419.56,1.34
20260617,628,640,625,640,1844000,560.13,14.26,582.55,426.13,1.34
20260618,657,700,657,700,5038000,571.79,22.42,592.65,434.09,3.6
20260622,705,758,683,691,25308000,581.72,18.78,601.1,441.92,9.58
20260623,717,718,650,657,17152000,588,11.74,606.7,449.08,4.94
20260624,632,640,616,638,9493000,592.16,7.74,611.95,455.56,2.42
20260625,651,651,621,630,8573000,595.32,5.83,615.45,462.11,1.98
20260626,628,650,570,570,15194000,593.21,-3.91,616.3,467.72,3.01
20260629,574,578,538,546,9290000,589.27,-7.34,613.2,472.88,1.69
20260630,570,600,568,600,9614000,590.17,1.67,609.8,478.82,1.62
20260701,626,639,580,587,12352000,589.9,-0.49,607.8,484.77,1.89
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 55.98
- over_600_ratio: 54.34
- over_800_ratio: 51.68
- over_1000_ratio: 48.76
- over_400_change_1w: -1.15
- over_800_change_1w: -0.45
- over_1000_change_1w: -1.9
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.51,,50.39,,48.92,,0,False,False
20260508,60.08,4.57,54.7,4.31,52.21,3.29,1,True,True
20260515,58.24,-1.84,53.48,-1.22,51.22,-0.99,0,False,False
20260522,60.4,2.16,55.56,2.08,53.02,1.8,1,True,True
20260529,60.67,0.27,55.62,0.06,53.42,0.4,2,True,True
20260605,56.38,-4.29,51.35,-4.27,49.56,-3.86,0,False,False
20260612,56.22,-0.16,51.2,-0.15,49.73,0.17,1,False,True
20260618,57.13,0.91,52.13,0.93,50.66,0.93,2,True,True
20260626,55.98,-1.15,51.68,-0.45,48.76,-1.9,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 8358 | 金居 | revenue_pullback | 營收成長股價回檔 | 76.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/24 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                  最近一月單月     去年同月       與去年同期增減%                   (115年5月)    (114年5月) ----------------------------------------------------------------- 營業收入(百萬元)      942              666           41.4% 稅前淨利(百萬元)      226               56          303.6% 歸屬母公司業主 淨利(百萬元)          181               44          311.4% 每股盈餘 (元)        0.72             0.18          300.0% ================================================================= (2)單季                   最近一季單季    去年同期        與去年同期增減%                   (115第1季)      (114第1季) ----------------------------------------------------------------- 營業收入(百萬元)     2,532            1,728          46.5% 稅前淨利(百萬元)       649              330          96.7% 歸屬母公司業主 淨利(百萬元)           520              265          96.2% 每股盈餘 (元)         2.06             1.05          96.2% ================================================================= (3)最近四季累計                 (114年第2季至115年第1季) ----------------------------------------------------------------- 營業收入(百萬元)            8,684 稅前淨利(百萬元)            1,660 歸屬母公司業主 淨利(百萬元)                1,318 每股盈餘 (元)                5.22 公司每股面額:10元 ================================================================= 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: 註1：以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製 之合併數，未經會計師查核(閱)，僅供投資人參考。 註2：最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字， 且係本公司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 註3：最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數， 業經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 8358 | 金居 | 8 | 6 | 5 | 8 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
