# INDIVIDUAL STOCK CHATGPT PACKET - 6291 沛亨

## Metadata
- generated_at: 2026-09-19 22:17:17 Asia/Taipei
- stock_id: 6291
- stock_name: 沛亨
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6291_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6291_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6291_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6291_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6291_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6291_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6291_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6291_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6291_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6291_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6291_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6291_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6291.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6291.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6291.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6291.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6291_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6291_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6291_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

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
- date: 20260918
- open: 523
- high: 525
- low: 500
- close: 524
- volume: 2372000
- ma5: 488.8
- ema23_primary: 452.3
- distance_to_ema23_pct: 15.85
- ma20: 447.68
- ma60: 425.35
- ma120: 458.75
- return_5d: 9.62
- return_20d: 34.88
- volume_ratio: 1.27
- distance_to_ma20_pct_auxiliary: 17.05
- distance_to_high_60_pct: -19.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,388.5,391.5,366,366,482000,385.35,-5.02,365.48,463.39,0.86
20260825,359,384,352,383.5,446000,385.2,-0.44,367.85,458.47,0.81
20260826,384,407.5,381,400,962000,386.43,3.51,372.1,454.33,1.73
20260827,403.5,437,392.5,417,1319000,388.98,7.2,378.05,450.95,2.2
20260828,430,430,394.5,400.5,1329000,389.94,2.71,381.88,447.38,2.05
20260831,391,407,388,405,530000,391.2,3.53,385.45,444.29,0.82
20260901,405,434,405,424,759000,393.93,7.63,388.32,441.26,1.15
20260902,423.5,465.5,423.5,440,2114000,397.77,10.62,391.32,439.16,2.99
20260903,453,484,453,458,4296000,402.79,13.71,395.07,437.49,4.78
20260904,470,477,436.5,456.5,2689000,407.26,12.09,399.27,436.72,2.65
20260907,457,459.5,440.5,442.5,1166000,410.2,7.87,402.23,435.84,1.11
20260908,458,483,458,463.5,2739000,414.64,11.78,407.1,434.63,2.36
20260909,474,506,473.5,480,2575000,420.09,14.26,410.98,433.37,2.06
20260910,473,503,471,495,2499000,426.33,16.11,416.38,432.55,1.89
20260911,486.5,492.5,471.5,478,1429000,430.64,11,421.02,431.93,1.04
20260914,460.5,484.5,440,466.5,2127000,433.63,7.58,424.68,430.57,1.46
20260915,459,467.5,445,446,883000,434.66,2.61,428.25,428.16,0.6
20260916,446,490.5,446,490.5,1669000,439.31,11.65,433.98,427.28,1.09
20260917,494.5,539,494.5,517,4828000,445.78,15.98,440.9,426.52,2.74
20260918,523,525,500,524,2372000,452.3,15.85,447.68,425.35,1.27
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 62.85
- over_600_ratio: 62.85
- over_800_ratio: 62.85
- over_1000_ratio: 62.85
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,64.04,-1.31,62.85,0,62.85,0,0,False,False
20260709,64.04,0,62.85,0,62.85,0,0,False,False
20260717,64.04,0,62.85,0,62.85,0,0,False,False
20260724,63.86,-0.18,62.85,0,62.85,0,0,False,False
20260731,63.86,0,62.85,0,62.85,0,0,False,False
20260807,62.85,-1.01,62.85,0,62.85,0,0,False,False
20260814,62.85,0,62.85,0,62.85,0,0,False,False
20260821,62.85,0,62.85,0,62.85,0,0,False,False
20260828,62.85,0,62.85,0,62.85,0,0,False,False
20260904,63.81,0.96,62.85,0,62.85,0,1,False,False
20260911,62.85,-0.96,62.85,0,62.85,0,0,False,False
20260918,62.85,0,62.85,0,62.85,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6291 | 沛亨 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 55.0 |  |  | neckline_challenge |  |  | continued_overheated | 1.董事會決議日期:115/09/16 2.私募有價證券種類:普通股 3.私募對象及其與公司間關係: (1)本次募集普通股之對象依證券交易法第43條之6及金融監督管理委員會相關函釋規    定之特定人，並以策略性投資人為限。 (2)已洽定之應募對象名稱與公司之關係如下:    應募人    與公司之關係    -------   -----------    林清源       無    陳麗雲       無    李彥昌       無 4.私募股數或張數:總私募股數為741,600股。 5.得私募額度:預計募集資金為新台幣241,020,000元。 6.私募價格訂定之依據及合理性: (1)本次私募普通股參考價格之訂定，以不低於下列二基準計算價格較高者之七成訂 定之。 a.依定價日前一、三或五個營業日擇一計算之本公司普通股收盤價簡單算數平均   數扣除無償配股除權及配息，並加回減資反除權後之股價。（為新台幣463.5元） b.依定價日前三十個營業日普通股收盤價簡單算數平均數扣除無償配股除權及配息，   並加回減資反除權後之股價。（經計算為新台幣413.08元） (2)以上二基準計價較高者新台幣463.5元為本次參考價格。   經綜合考量後，實際私募價格訂為每股新台幣325元，為參考價格之70.12%，   未低於股東會決議之參考價格之七成。 7.本次私募資金用途:充實營運資金及其他因應公司未來長期發展所需資金。 8.不採用公開募集之理由: 本公司為充實營運資金及因應公司長期發展所需，爰有資金需求，故考量以私募方式 相對具迅速簡便之時效性及私募有價證券受限於三年內不得自由轉讓規定，將可更為 確保公司與策略性夥伴間之長期合作關係，並達到迅速挹注所需資金之目的。 9.獨立董事反對或保留意見:無 10.實際定價日:115年9月16日 11.參考價格:新台幣463.5元。 12.實際私募價格、轉換或認購價格:每股新台幣325元。 13.本次私募新股之權利義務:原則上與本公司已發行之普通股相同，惟本私募案之普 通股於交付日起三年內除據證券交易法第四十三條之八規定外，均不得自由轉讓。 本公司於發行滿三年後，擬依證券交易法相關規定向主管機關提出上櫃申請。 14.附有轉換、交換或認股者，其換股基準日:不適用 15.附有轉換、交換或認股者，對股權可能稀釋情形:不適用 16.附有轉換或認股者，於私募公司債交付且假設全數轉換或認購普通股後對上櫃普通股 股權比率之可能影響（上櫃普通股數A、A/已發行普通股）:不適用 17.前項預計上櫃普通股未達500萬股且未達25%者，請說明股權流通性偏低之因應措施: 不適用 18.其他應敘明事項: (1)本次私募普通股繳款期間自115年9月16日至115年9月30日止。 (2)私募增資基準日：115年9月30日。 (3)有關本次私募增資發行新股之後續相關事宜擬授權董事長依法令規定全權辦理之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6291 | 沛亨 | 3 | 3 | 4 | 9 | 12 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
