# INDIVIDUAL STOCK CHATGPT PACKET - 1727 中華化

## Metadata
- generated_at: 2026-10-06 22:16:50 Asia/Taipei
- stock_id: 1727
- stock_name: 中華化
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1727_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1727_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1727.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1727.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1727.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1727.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1727_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1727_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1727_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: high_level_distribution_risk
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
- date: 20261002
- open: 111
- high: 123
- low: 111
- close: 123
- volume: 35901281
- ma5: 115.6
- ema23_primary: 103.14
- distance_to_ema23_pct: 19.26
- ma20: 101.25
- ma60: 89.05
- ma120: 86.54
- return_5d: 5.58
- return_20d: 30.57
- volume_ratio: 2.74
- distance_to_ma20_pct_auxiliary: 21.48
- distance_to_high_60_pct: -1.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,94.1,95.1,89.1,89.2,3460712,88.53,0.76,87.58,85.78,0.59
20260904,90,95.2,88.2,94.7,5890316,89.04,6.35,88.7,85.9,0.96
20260907,94.7,95.4,90.8,91,4256734,89.21,2.01,89.43,85.99,0.68
20260908,91.5,92.3,90.5,90.6,1525491,89.32,1.43,90.13,86.08,0.25
20260909,90.5,92.7,90.2,91.1,1513988,89.47,1.82,90.72,86.17,0.25
20260910,90,92.4,89.9,90.4,1132611,89.55,0.95,91.42,86.25,0.19
20260911,89.1,92.3,89,89.6,1398176,89.55,0.05,92.14,86.18,0.23
20260914,89,89.7,86.2,88.2,1593169,89.44,-1.39,92.42,86.08,0.27
20260915,88,92.8,87.6,90.1,2685038,89.49,0.68,92.47,85.89,0.51
20260916,91.5,98.7,90.9,95.6,8782788,90,6.22,92.62,85.87,1.82
20260917,98.7,105,97.7,105,15353455,91.25,15.06,93.29,86.04,2.93
20260918,105,109.5,102,106,16587496,92.48,14.62,94.08,86.25,2.87
20260921,107,109.5,100.5,103,7483460,93.36,10.33,94.73,86.5,1.25
20260922,103,107,99.6,106,6851763,94.41,12.27,95.47,86.8,1.12
20260923,105,116.5,103,116.5,21402346,96.25,21.04,96.57,87.24,3.13
20260924,114,125,109,115.5,47932996,97.86,18.03,97.5,87.64,5.43
20260929,113,122,104,118.5,29773336,99.58,19,98.52,88.08,3
20260930,117,117,108,109,29883184,100.36,8.61,98.97,88.35,2.74
20261001,108,116,105.5,112,18550381,101.33,10.53,99.81,88.53,1.62
20261002,111,123,111,123,35901281,103.14,19.26,101.25,89.05,2.74
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 61.58
- over_600_ratio: 59.74
- over_800_ratio: 58.03
- over_1000_ratio: 56.64
- over_400_change_1w: -7.29
- over_800_change_1w: -6.94
- over_1000_change_1w: -5.63
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,55.37,-1.06,51.16,-2.32,50.51,-1.52,0,False,False
20260724,54.51,-0.86,51.48,0.32,49.39,-1.12,1,False,True
20260731,54.48,-0.03,49.8,-1.68,49.8,0.41,2,False,True
20260807,54.44,-0.04,49.97,0.17,49.24,-0.56,3,False,True
20260814,54.13,-0.31,48.71,-1.26,48.71,-0.53,4,False,False
20260821,56.42,2.29,50.25,1.54,49.51,0.8,5,False,True
20260828,57.79,1.37,53.26,3.01,50.4,0.89,6,True,True
20260904,59.02,1.23,53.97,0.71,51.19,0.79,7,True,True
20260911,58.17,-0.85,51.65,-2.32,50.27,-0.92,0,False,False
20260918,64.88,6.71,58.5,6.85,57.82,7.55,1,True,True
20260924,68.87,3.99,64.97,6.47,62.27,4.45,2,True,True
20261002,61.58,-7.29,58.03,-6.94,56.64,-5.63,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 1727 | 中華化 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | continued_overheated | 1.事實發生日:115/10/01 2.公司名稱:臺灣中華化學工業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:理財周刊 6.報導內容:理財周刊：外資大買296億、狂掃面板雙虎16萬張！中華化結親台塑卻淪 賣超王 翻開中華化(1727)2026年第二季的資產負債表： 公司整體的總資產只有 38.02億元。 股東權益(淨值)只有 21.60億元。 帳上躺著的現金及約當現金，更是只有少得可憐的 約1.70億元！ 然而，中華化董事會授權的合資投資上限，竟然高達 30億元(持股50%)！ 這筆30億元的資本承諾，整整佔了中華化總資產的79%，更是其全公司股東權益的 139%！ 一個帳上只有1.7億現金的小型特化廠，要去扛一筆高達30億元、耗時數年的建廠資 本支出，錢從哪裡來？是找銀行大舉借貸背上沉重利息。 7.發生緣由:澄清媒體報導 8.因應措施:無 9.其他應敘明事項: (1)有關媒體報導所稱「超過淨值百倍的龐大負債」一節，與事實不符。本公司截至115 年第2季合併財務報告之歸屬於母公司業主之權益約為新臺幣21.6億元；本案所涉新臺 幣30億元係本公司投資金額上限，並非已發生之負債，若以30億元與21.6億元比較，約 為1.39倍，並非報導所稱之百倍。 (2)有關媒體報導本案為「中華化投入30億元、台塑投入12億元」一節，與本公司董事 會決議內容不符。本案規劃由本公司投資金額上限新臺幣30億元，取得合資公司50%股 權；另由臺灣塑膠工業股份有限公司、臺灣化學纖維股份有限公司、台塑石化股份有限 公司及台塑生醫科技股份有限公司等台塑企業四家公司合計投資新臺幣30億元，取得50% 股權，雙方共同組成50：50之策略性合資架構。 (3)本案所涉新臺幣30億元係本公司多年期之股權投資上限，並非一次性於短期內支付， 亦非新增負債。以單一季度期末現金餘額與多年期投資上限直接比較，尚不足以完整反 映公司整體資金規劃、營運現金流、融資安排及後續投資時程。 (4)有關媒體提及外資單日賣超本公司股票8,650張，該交易量屬市場交易資料；惟進一 步將該交易結果解讀為「外資認定本公司具有致命融資風險」之說法，並非本公司已公 開資訊所能支持之結論。本公司不對股價及個別投資人之交易行為置評，並將持續以實 際營運成果、投資計畫執行進度及財務紀律接受市場檢驗。 (5)本公司再次強調，本案係為拓展電子級硫酸事業、整合雙方資源所推動之策略性合 資案，相關投資將依既定程序及實際進度辦理。本公司將審慎進行資金規劃及投資管理 ，以兼顧公司營運、財務健全及股東權益。 (6)以上說明係針對媒體報導內容之事實澄清，實際投資執行仍以本公司依法公告之資 訊及後續相關程序為準。；calendar event: ex_right on 20261013; status=confirmed; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 1727 | 中華化 | 7 | 1 | 5 | 8 | 16 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 1727 | 中華化 | 35 | 0 | 22475950.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
