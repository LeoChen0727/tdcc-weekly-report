# INDIVIDUAL STOCK CHATGPT PACKET - 2023 燁輝

## Metadata
- generated_at: 2026-10-08 22:17:07 Asia/Taipei
- stock_id: 2023
- stock_name: 燁輝
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 366
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2023_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2023_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2023_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2023_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2023_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2023_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2023_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2023_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2023_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2023_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2023_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2023_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2023.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2023.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2023.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2023.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2023_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2023_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2023_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20261002
- open: 13.75
- high: 14
- low: 13.75
- close: 13.9
- volume: 1588195
- ma5: 13.73
- ema23_primary: 13.76
- distance_to_ema23_pct: 1.02
- ma20: 13.78
- ma60: 13.81
- ma120: 13.83
- return_5d: 2.21
- return_20d: 0.36
- volume_ratio: 1.48
- distance_to_ma20_pct_auxiliary: 0.89
- distance_to_high_60_pct: -4.47

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,13.8,13.9,13.75,13.8,440101,13.83,-0.2,13.84,13.79,0.46
20260904,13.9,13.9,13.7,13.85,743607,13.83,0.15,13.84,13.79,0.76
20260907,13.95,13.95,13.75,13.95,680478,13.84,0.8,13.85,13.8,0.7
20260908,13.95,14.05,13.9,13.95,1092052,13.85,0.73,13.85,13.8,1.09
20260909,13.9,14.05,13.9,14,656027,13.86,1,13.86,13.8,0.66
20260910,13.9,14.2,13.9,14.1,1308048,13.88,1.57,13.88,13.8,1.28
20260911,14,14.05,13.85,13.9,893275,13.88,0.12,13.89,13.8,0.88
20260914,13.8,13.9,13.8,13.85,454384,13.88,-0.22,13.9,13.8,0.45
20260915,13.8,13.85,13.6,13.7,1486524,13.87,-1.19,13.89,13.8,1.43
20260916,13.75,13.8,13.6,13.7,2070388,13.85,-1.09,13.88,13.8,1.87
20260917,13.7,13.75,13.65,13.7,748868,13.84,-1,13.87,13.8,0.71
20260918,13.85,13.85,13.6,13.6,2143416,13.82,-1.58,13.85,13.8,1.91
20260921,13.7,13.7,13.6,13.6,847867,13.8,-1.45,13.83,13.8,0.75
20260922,13.65,13.65,13.55,13.6,786965,13.78,-1.33,13.82,13.8,0.7
20260923,13.65,13.65,13.55,13.6,441676,13.77,-1.22,13.8,13.8,0.4
20260924,13.65,13.7,13.55,13.65,765267,13.76,-0.79,13.79,13.8,0.7
20260929,13.65,13.85,13.55,13.55,1159080,13.74,-1.39,13.79,13.8,1.09
20260930,13.7,13.8,13.7,13.75,1279312,13.74,0.06,13.77,13.8,1.26
20261001,13.85,14.1,13.75,13.8,1896256,13.75,0.39,13.78,13.8,1.85
20261002,13.75,14,13.75,13.9,1588195,13.76,1.02,13.78,13.81,1.48
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 79.38
- over_600_ratio: 78.52
- over_800_ratio: 78.03
- over_1000_ratio: 77.59
- over_400_change_1w: 0
- over_800_change_1w: 0.04
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,79.03,0.14,77.81,0.19,77.54,0.2,3,True,True
20260724,79.03,0,77.71,-0.1,77.44,-0.1,4,False,False
20260731,79.27,0.24,77.89,0.18,77.62,0.18,5,True,True
20260807,79.34,0.07,77.95,0.06,77.57,-0.05,6,False,True
20260814,79.35,0.01,78.04,0.09,77.62,0.05,7,True,True
20260821,79.36,0.01,78.06,0.02,77.68,0.06,8,True,True
20260828,79.2,-0.16,77.7,-0.36,77.41,-0.27,0,False,False
20260904,79.25,0.05,77.8,0.1,77.46,0.05,1,True,True
20260911,79.37,0.12,78,0.2,77.72,0.26,2,True,True
20260918,79.38,0.01,78.07,0.07,77.79,0.07,3,True,True
20260924,79.38,0,77.99,-0.08,77.61,-0.18,0,False,False
20261002,79.38,0,78.03,0.04,77.59,-0.02,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2023 | 燁輝 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | 1.董事會決議日期:115/09/29 2.買回股份目的:維護公司信用及股東權益 3.買回股份種類:普通股 4.買回股份總金額上限(元):6,492,888,140 5.預定買回之期間:115/09/30~115/11/28 6.預定買回之數量(股):15,000,000 7.買回區間價格(元):13.00~15.50，公司股價低於區間價格下限，將繼續買回 8.買回方式:自集中交易市場買回 9.預定買回股份占公司已發行股份總數之比率(%):0.82 10.申報時已持有本公司股份之累積股數(股):24,138,000 11.申報前五年內買回公司股份之情形: (1)實際買回股份期間：115/07/28 ~ 115/09/22 、預定買回股數(股)：15000000 、實際已買回股數 (股)：7840000 、執行情形(實際已買回股數占預定買回股數%)：52.00 (2)實際買回股份期間：115/05/27 ~ 115/07/20 、預定買回股數(股)：20000000 、實際已買回股數 (股)：16298000 、執行情形(實際已買回股數占預定買回股數%)：81.00 (3)實際買回股份期間：115/04/24 ~ 115/05/26 、預定買回股數(股)：20000000 、實際已買回股數 (股)：20000000 、執行情形(實際已買回股數占預定買回股數%)：100.00 (4)實際買回股份期間：115/03/06 ~ 115/04/23 、預定買回股數(股)：20000000 、實際已買回股數 (股)：20000000 、執行情形(實際已買回股數占預定買回股數%)：100.00 (5)實際買回股份期間：115/01/09 ~ 115/03/05 、預定買回股數(股)：15000000 、實際已買回股數 (股)：15000000 、執行情形(實際已買回股數占預定買回股數%)：100.00 (6)實際買回股份期間：114/11/18 ~ 115/01/06 、預定買回股數(股)：15000000 、實際已買回股數 (股)：15000000 、執行情形(實際已買回股數占預定買回股數%)：100.00 (7)實際買回股份期間：114/10/14 ~ 114/11/17 、預定買回股數(股)：12000000 、實際已買回股數 (股)：12000000 、執行情形(實際已買回股數占預定買回股數%)：100.00 (8)實際買回股份期間：114/08/13 ~ 114/10/03 、預定買回股數(股)：15000000 、實際已買回股數 (股)：7880000 、執行情形(實際已買回股數占預定買回股數%)：53.00 (9)實際買回股份期間：114/06/10 ~ 114/08/08 、預定買回股數(股)：20000000 、實際已買回股數 (股)：15236000 、執行情形(實際已買回股數占預定買回股數%)：76.00 (10)實際買回股份期間：114/04/09 ~ 114/06/06 、預定買回股數(股)：30000000 、實際已買回股 數(股)：25641000 、執行情形(實際已買回股數占預定買回股數%)：85.00 (11)實際買回股份期間：114/01/02 ~ 114/01/20 、預定買回股數(股)：15000000 、實際已買回股 數(股)：7220000 、執行情形(實際已買回股數占預定買回股數%)：48.00 (12)實際買回股份期間：113/12/05 ~ 113/12/31 、預定買回股數(股)：15000000 、實際已買回股 數(股)：15000000 、執行情形(實際已買回股數占預定買回股數%)：100.00 (13)實際買回股份期間：113/11/06 ~ 113/12/04 、預定買回股數(股)：10000000 、實際已買回股 數(股)：10000000 、執行情形(實際已買回股數占預定買回股數%)：100.00 (14)實際買回股份期間：112/10/17 ~ 112/11/14 、預定買回股數(股)：20000000 、實際已買回股 數(股)：3860000 、執行情形(實際已買回股數占預定買回股數%)：19.00 (15)實際買回股份期間：112/08/15 ~ 112/10/13 、預定買回股數(股)：20000000 、實際已買回股 數(股)：16673000 、執行情形(實際已買回股數占預定買回股數%)：83.00 (16)實際買回股份期間：112/05/05 ~ 112/06/15 、預定買回股數(股)：20000000 、實際已買回股 數(股)：10021000 、執行情形(實際已買回股數占預定買回股數%)：50.00 (17)實際買回股份期間：111/10/19 ~ 111/12/12 、預定買回股數(股)：30000000 、實際已買回股 數(股)：9233000 、執行情形(實際已買回股數占預定買回股數%)：31.00 12.已申報買回但未執行完畢之情形: 為兼顧市場機制及維護整體股東權益，考量股價變動已趨&#31311;定，故未予以全部執行完畢。 13.董事會決議買回股份之會議紀錄: 案由:本公司為維護股東權益擬依證券交易法28條之2及「上市上櫃公司買回本公司股份辦法」規定於集 中交易市場買回本公司股份。 說  明：一、本次擬買回本公司股份相關條件如下： (一)買回股份目的：為維護本公司信用及股東權益。 (二)買回股份種類：普通股。 (三)買回股份總金額上限：新台幣6,492,888,140元。 (四)買回期間及數量：本公司本次預定買回股數共計15,000,000股，設定買回期間為115年09月30日至 115年11月28日。 (五)買回區間價格：每股單價在新台幣13.0元至15.5元；惟若股價低於前述區間價格下限時，本公司將 繼續執行買回公司股份。 (六)買回方式：自有價證券集中交易市場買回。  二、本次預定買回股份佔本公司已發行股份之0.82%，不足以影響本公司財務狀況及資本之維持，擬由 董事會出具買回公司股份不影響公司資本維持之聲明書(詳如附件二)。  三、本公司買回之區間價格尚屬合理，檢附會計師買回股份價格之合理性評估意見書(詳如附件三)。 14.「上市上櫃公司買回本公司股份辦法」第十條規定之轉讓辦法: 不適用 15.「上市上櫃公司買回本公司股份辦法」第十一條規定之轉換或認股辦法: 不適用 16.董事會已考慮公司財務狀況，不影響公司資本維持之聲明: 董事會聲明書 一、本公司經115年09月29日第十二次董事會三分之二以上董事之出席及出席董事超過二分之一之 同意通過，自申報日起二個月內，即115年09月30日至115年11月28日於集中交易市場﹙證券商營業處 所﹚買回本公司股份15,000,000股。 二、上述買回股份總數，僅占本公司已發行股份之0.82%，且買回股份所需金額上限僅占本公司流動資產 之0.85%，茲聲明本公司董事會已考慮公司財務狀況，上述股份之買回並不影響本公司資本之維持。 三、本聲明書業經本公司上述同次董事會議通過，出席董事五人同意本聲明書之內容，併此聲明。  燁輝企業股份有限公司董事長：林義守 17.會計師或證券承銷商對買回股份價格之合理性評估意見: 會計師認為燁輝企業股份有限公司預計以每股13.0元~15.5元買回自身公司之股票，對其相關財務資料及財 務結構等並無重大影響，且其經董事會擬決議預定買回股份之區間價格尚屬合理。 18.其他證期局所規定之事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2023 | 燁輝 | 1 | 1 | 2 | 2 | 4 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
