# INDIVIDUAL STOCK CHATGPT PACKET - 1815 富喬

## Metadata
- generated_at: 2026-09-26 15:51:04 Asia/Taipei
- stock_id: 1815
- stock_name: 富喬
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: True
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1815_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1815_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1815_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1815_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1815_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1815_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1815_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1815_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1815_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1815_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1815_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1815_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1815.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1815.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1815.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1815.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1815_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1815_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1815_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260924
- open: 119.5
- high: 119.5
- low: 115
- close: 116
- volume: 28287000
- ma5: 119.7
- ema23_primary: 117.09
- distance_to_ema23_pct: -0.93
- ma20: 122.92
- ma60: 100.58
- ma120: 103.53
- return_5d: 3.57
- return_20d: -0.43
- volume_ratio: 0.41
- distance_to_ma20_pct_auxiliary: -5.63
- distance_to_high_60_pct: -18.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,118.5,128,111,125.5,127211000,99.82,25.73,97.2,93.29,2.55
20260831,124,128,122.5,126.5,79965000,102.04,23.97,99.89,93.67,1.5
20260901,126.5,132.5,125,129,68487000,104.29,23.7,102.33,94.12,1.23
20260902,128.5,139,126,131,121340000,106.51,22.99,104.69,94.69,2.02
20260903,132,139.5,118,120,120272000,107.64,11.49,106.34,95.04,1.88
20260904,125.5,126,114,118.5,50020000,108.54,9.17,107.97,95.49,0.77
20260907,124,130,123.5,130,70385000,110.33,17.83,110.02,96.15,1.07
20260908,131,141.5,123,135,114345000,112.39,20.12,112.33,96.8,1.6
20260909,134,135,126,126,68959000,113.52,10.99,114.14,97.31,0.92
20260910,125,129,124,126,43268000,114.56,9.99,115.94,97.83,0.56
20260911,125,129,122,127.5,44139000,115.64,10.26,117.74,98.38,0.56
20260914,126,127,119.5,120,52185000,116,3.45,118.92,98.74,0.65
20260915,119,121.5,114.5,114.5,45520000,115.88,-1.19,119.88,98.88,0.57
20260916,115.5,121.5,115.5,118.5,43016000,116.1,2.07,120.9,99.17,0.54
20260917,119,119.5,111,112,52764000,115.75,-3.24,121.15,99.27,0.7
20260918,118,123,117.5,119.5,95458000,116.07,2.96,121.53,99.47,1.29
20260921,121.5,124.5,120,121,66057000,116.48,3.88,122.2,99.88,0.89
20260922,125,129.5,120,122,69858000,116.94,4.33,122.85,100.23,0.92
20260923,122.5,124.5,119.5,120,32320000,117.19,2.4,122.95,100.38,0.45
20260924,119.5,119.5,115,116,28287000,117.09,-0.93,122.92,100.58,0.41
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 51.9
- over_600_ratio: 50.43
- over_800_ratio: 49.51
- over_1000_ratio: 48.41
- over_400_change_1w: 0.52
- over_800_change_1w: 1.04
- over_1000_change_1w: 0.75
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,34.08,-1.85,31.87,-2.29,30.92,-1.7,0,False,False
20260717,32.54,-1.54,30.94,-0.93,30.15,-0.77,0,False,False
20260724,32.47,-0.07,30.64,-0.3,29.71,-0.44,1,False,False
20260731,32,-0.47,30.22,-0.42,29.25,-0.46,0,False,False
20260807,33.34,1.34,31.34,1.12,30.7,1.45,1,True,True
20260814,33.16,-0.18,31.43,0.09,30.44,-0.26,2,False,True
20260821,41.28,8.12,39.16,7.73,37.59,7.15,3,True,True
20260828,49.45,8.17,46.88,7.72,45.13,7.54,4,True,True
20260904,55.55,6.1,53.09,6.21,52.01,6.88,5,True,True
20260911,56.97,1.42,54.05,0.96,52.93,0.92,6,True,True
20260918,51.38,-5.59,48.47,-5.58,47.66,-5.27,0,False,False
20260924,51.9,0.52,49.51,1.04,48.41,0.75,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1815 | 富喬 | revenue_pullback | 營收成長股價回檔 | 77.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/08/24 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除權息 3.發放普通股股利種類及金額: (1)現金股利：新台幣292,439,744元(每股配發新台幣0.50001709元)。 (2)股票股利：盈餘轉增資發行普通股29,243,975股(每仟股無償配發50.00171092股)。 4.除權（息）交易日:115/09/09 5.最後過戶日:115/09/10 6.停止過戶起始日期:115/09/11 7.停止過戶截止日期:115/09/15 8.除權（息）基準日:115/09/15 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/10/13 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項: (1)因收回限制員工權利新股，致流通在外股數變動，故調整配股息率。 (2)新股權利證書預訂於115年10月13日（星期二）直接劃撥至股東之臺灣集中保管結 算所股份有限公司證券存摺帳戶中，並於同日上櫃買賣，股東不得請求交付新股權利 證書。上述股票俟呈奉主管機關核准資本額變更登記後三十日內以無實體發行，以上 新股權利證書劃撥暨上櫃日期，若因故而有變動，以本公司另行公告日期為準。 (3)現金股利由本公司股務室以匯款或掛號郵寄「禁止背書轉讓」支票方式發放， 郵匯費由股東支付，應發股利新台幣30元(含)以下者，請股東持相關文件和原留印鑑 親洽或郵寄本公司股務室領取。現金股利發放至元為止(元以下捨去)，配發不足一元 之畸零款，轉入公司其他收入項下。 (4)凡參加帳簿劃撥配發股票之股東，其未滿一股之畸零股款，將充抵股東集保帳簿劃 撥之費用。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1815 | 富喬 | 11 | 10 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
