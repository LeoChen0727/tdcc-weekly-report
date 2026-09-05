# INDIVIDUAL STOCK CHATGPT PACKET - 3498 陽程

## Metadata
- generated_at: 2026-09-05 15:53:22 Asia/Taipei
- stock_id: 3498
- stock_name: 陽程
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3498_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3498_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3498_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3498_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3498.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3498.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3498.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3498.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3498_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3498_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3498_latest.md?ref=main

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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: high_level_consolidation
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
- date: 20260904
- open: 197.5
- high: 201
- low: 185.5
- close: 194
- volume: 3414000
- ma5: 199.8
- ema23_primary: 174.34
- distance_to_ema23_pct: 11.28
- ma20: 178.07
- ma60: 136.1
- ma120: 119.58
- return_5d: 2.37
- return_20d: 66.52
- volume_ratio: 1.16
- distance_to_ma20_pct_auxiliary: 8.94
- distance_to_high_60_pct: -12.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,118.5,127,118,125,2005000,111.16,12.45,109.31,124.05,1.12
20260811,130,131,121.5,124.5,2484000,112.27,10.89,109.56,123.64,1.47
20260812,126,133,124.5,131,2159000,113.83,15.08,109.97,123.41,1.26
20260813,144,144,144,144,1713000,116.34,23.77,110.69,123.54,1.02
20260814,154,158,154,158,6192000,119.82,31.87,112.74,123.78,3.31
20260817,159.5,168.5,155.5,158.5,7914000,123.04,28.82,115.19,123.98,3.64
20260818,158.5,174,153.5,174,6519000,127.29,36.7,118.61,124.21,2.7
20260819,170,190.5,169,190.5,3043000,132.55,43.71,122.56,124.74,1.22
20260820,190.5,190.5,176,183.5,2137000,136.8,34.14,126.02,125.21,0.84
20260821,185.5,193,182,192,1582000,141.4,35.79,130.04,125.82,0.61
20260824,191,200.5,180,185,970000,145.03,27.56,133.89,126.49,0.37
20260825,185.5,200,180.5,200,995000,149.61,33.68,138.93,127.31,0.4
20260826,195.5,205,195.5,203.5,508000,154.1,32.05,144.44,128.3,0.21
20260827,208,208,199,203.5,393000,158.22,28.62,150.3,129.35,0.17
20260828,200,203,189,189.5,1152000,160.83,17.83,155.28,130.21,0.49
20260831,191,208,191,208,1452000,164.76,26.25,160.72,131.46,0.61
20260901,215.5,217,194.5,203.5,4768000,167.99,21.14,165.72,132.68,1.89
20260902,203,213,195,201.5,3075000,170.78,17.99,170.15,133.91,1.18
20260903,216,221.5,191,192,6524000,172.55,11.27,174.2,134.91,2.27
20260904,197.5,201,185.5,194,3414000,174.34,11.28,178.07,136.1,1.16
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 56.92
- over_600_ratio: 55.32
- over_800_ratio: 53.13
- over_1000_ratio: 51.74
- over_400_change_1w: -0.34
- over_800_change_1w: 0.99
- over_1000_change_1w: 0.95
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,51.39,-0.03,46.76,-0.59,45.14,-2.21,0,False,False
20260626,50.6,-0.79,47.72,0.96,45.01,-0.13,1,False,True
20260703,51.84,1.24,48.31,0.59,46.89,1.88,2,True,True
20260709,49.16,-2.68,43.94,-4.37,43.94,-2.95,0,False,False
20260717,48.9,-0.26,42.29,-1.65,39.52,-4.42,0,False,False
20260724,48.41,-0.49,43.97,1.68,39.82,0.3,1,False,True
20260731,48.4,-0.01,42.14,-1.83,42.14,2.32,2,False,True
20260807,47.65,-0.75,42.51,0.37,42.51,0.37,3,False,True
20260814,50.22,2.57,45.1,2.59,45.1,2.59,4,True,True
20260821,57.33,7.11,51.3,6.2,49.79,4.69,5,True,True
20260828,57.26,-0.07,52.14,0.84,50.79,1,6,False,True
20260904,56.92,-0.34,53.13,0.99,51.74,0.95,7,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3498 | 陽程 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | continued_overheated | 1.法律事件之當事人:上海陽程科技有限公司 2.法律事件之法院名稱或處分機關:河南省林州市人民法院 3.法律事件之相關文書案號:河南省林州市人民法院判決書                        （2025）豫0581民初7776號 4.事實發生日:115/07/09 5.發生原委(含爭訟標的):本公司之子公司上海陽程科技有限公司於2020年9月委由 北京市道成律師事務所，處理上海陽程科技有限公司與林州致遠電子科技有限公司間 承攬合同糾紛案說判決說明。 判決結果： 我方總計須在判決生效後 15 日內支付給原告人民幣23,998,347.23元，明細如下： ‧賠償金：人民幣23,163,739.23元（含已維修費、未維修貶值、停產及品質損失）。 ‧鑑定費：人民幣689,900元。 ‧案件受理費：人民幣139,708元。 ‧保全申請費：人民幣5,000元。 6.處理過程:提出上訴並持續與律師溝通。 7.對公司財務業務影響及預估影響金額:本案本公司已提列足額損失準備， 對財務業務無重大影響。因先前對造超額聲請財產保全應付予本公司貨款， 若依本次判決結果，本公司可聲請發還約人民幣789萬元之款項。 8.因應措施及改善情形: 本公司認為，原審裁判結果顯流於地方保護主義，對於本公司提出之多處明顯爭點未予 審酌，更刻意迴避訴訟時效等重大法律事實，在無法律依據下全盤採納對造主張，其 認事用法顯失公正。 為維護本公司權益擬提起上訴。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第2款所定對 股東權益或證券價格有重大影響之事項):不適用；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3498 | 陽程 | 2 | 2 | 3 | 3 | 12 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
