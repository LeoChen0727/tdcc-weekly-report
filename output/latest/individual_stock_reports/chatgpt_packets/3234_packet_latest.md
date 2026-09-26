# INDIVIDUAL STOCK CHATGPT PACKET - 3234 光環

## Metadata
- generated_at: 2026-09-26 22:16:40 Asia/Taipei
- stock_id: 3234
- stock_name: 光環
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
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3234_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3234_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3234.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3234.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3234.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3234.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3234_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3234_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3234_latest.md?ref=main

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
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
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
- open: 163
- high: 180
- low: 162
- close: 178
- volume: 4252000
- ma5: 175.9
- ema23_primary: 175.21
- distance_to_ema23_pct: 1.59
- ma20: 186.43
- ma60: 144.96
- ma120: 129.43
- return_5d: 0.56
- return_20d: -1.11
- volume_ratio: 1.21
- distance_to_ma20_pct_auxiliary: -4.52
- distance_to_high_60_pct: -19.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,183,186,181,181.5,2192000,145.85,24.45,141.8,126.18,0.56
20260831,180,185,170,185,3259000,149.11,24.07,145.85,126.98,0.81
20260901,185,203,183.5,200,3479000,153.35,30.42,150.2,128.24,0.86
20260902,199,220,199,211,7818000,158.15,33.41,155,129.69,1.8
20260903,211,214,193.5,194.5,6156000,161.18,20.67,159.2,130.85,1.34
20260904,203,209,190,206,5383000,164.92,24.91,164.12,132.4,1.12
20260907,202,205.5,196,199.5,4173000,167.8,18.89,168.2,133.91,0.85
20260908,203.5,206.5,195.5,197,3055000,170.23,15.72,171.97,135.34,0.62
20260909,200,206,194,200,3375000,172.71,15.8,175.32,136.63,0.7
20260910,196,205.5,192.5,195,3324000,174.57,11.7,178.03,137.84,0.73
20260911,187,194.5,183.5,187.5,2880000,175.65,6.75,180.57,138.76,0.63
20260914,183,186.5,173,174,3402000,175.51,-0.86,181.78,139.24,0.77
20260915,172.5,173.5,163,163.5,2286000,174.51,-6.31,182.65,139.65,0.54
20260916,163.5,179.5,163.5,177.5,3095000,174.76,1.57,184.15,140.29,0.73
20260917,180,194,176,177,3747000,174.95,1.17,185.45,140.82,0.88
20260918,178.5,185,175,180,2640000,175.37,2.64,186.9,141.56,0.63
20260921,183.5,187,178.5,178.5,2088000,175.63,1.64,187.53,142.44,0.53
20260922,180.5,181,172.5,173,2342000,175.41,-1.37,187.05,143.3,0.65
20260923,174.5,174.5,169,170,1404000,174.96,-2.83,186.53,144.01,0.41
20260924,163,180,162,178,4252000,175.21,1.59,186.43,144.96,1.21
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 35.21
- over_600_ratio: 30.82
- over_800_ratio: 27.46
- over_1000_ratio: 26.11
- over_400_change_1w: 0.29
- over_800_change_1w: 0.01
- over_1000_change_1w: -1.34
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,33.03,0.04,25.12,0.03,23.61,0.16,3,True,True
20260717,31.36,-1.67,23.45,-1.67,22.69,-0.92,0,False,False
20260724,31.71,0.35,21.72,-1.73,20.96,-1.73,1,False,False
20260731,30.87,-0.84,21.82,0.1,21.06,0.1,2,False,True
20260807,31.11,0.24,21.49,-0.33,20.73,-0.33,3,False,False
20260814,32.99,1.88,23.41,1.92,21.89,1.16,4,True,True
20260821,33.94,0.95,25.66,2.25,23.27,1.38,5,True,True
20260828,36.24,2.3,27.38,1.72,25.86,2.59,6,True,True
20260904,36.21,-0.03,28.45,1.07,27.69,1.83,7,False,True
20260911,34.62,-1.59,27,-1.45,27,-0.69,0,False,False
20260918,34.92,0.3,27.45,0.45,27.45,0.45,1,False,True
20260924,35.21,0.29,27.46,0.01,26.11,-1.34,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3234 | 光環 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/09/21 2.公司名稱:光環科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:  (1)本公司已於民國115年5月29日股東常會決議通過發行限制員工權利新股普通股     共計1,000,000股，每股面額新台幣10元，發行總額為新台幣10,000,000元。     業經金融監督管理委員會於115年8月4日金管證發字第1150351320號函申報生效。  (2)本公司民國115年8月7日董事會授權董事長訂定:     本公司董事長訂定增資基準日為民國115年9月21日，本次發行股數為785,000股。 6.因應措施:不適用。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 3234 | 光環 | pullback_rebound | 回檔後短線轉強 | 83.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/09/21 2.公司名稱:光環科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:  (1)本公司已於民國115年5月29日股東常會決議通過發行限制員工權利新股普通股     共計1,000,000股，每股面額新台幣10元，發行總額為新台幣10,000,000元。     業經金融監督管理委員會於115年8月4日金管證發字第1150351320號函申報生效。  (2)本公司民國115年8月7日董事會授權董事長訂定:     本公司董事長訂定增資基準日為民國115年9月21日，本次發行股數為785,000股。 6.因應措施:不適用。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 3234 | 光環 | revenue_pullback | 營收成長股價回檔 | 83.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/09/21 2.公司名稱:光環科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:  (1)本公司已於民國115年5月29日股東常會決議通過發行限制員工權利新股普通股     共計1,000,000股，每股面額新台幣10元，發行總額為新台幣10,000,000元。     業經金融監督管理委員會於115年8月4日金管證發字第1150351320號函申報生效。  (2)本公司民國115年8月7日董事會授權董事長訂定:     本公司董事長訂定增資基準日為民國115年9月21日，本次發行股數為785,000股。 6.因應措施:不適用。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3234 | 光環 | 8 | 8 | 5 | 8 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
