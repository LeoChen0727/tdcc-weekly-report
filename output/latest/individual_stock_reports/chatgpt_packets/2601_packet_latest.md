# INDIVIDUAL STOCK CHATGPT PACKET - 2601 益航

## Metadata
- generated_at: 2026-09-05 22:16:06 Asia/Taipei
- stock_id: 2601
- stock_name: 益航
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 347
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2601_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2601_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2601.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2601.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2601.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2601.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2601_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2601_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2601_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260904
- open: 6.69
- high: 6.98
- low: 6.69
- close: 6.79
- volume: 1738088
- ma5: 6.78
- ema23_primary: 6.71
- distance_to_ema23_pct: 1.22
- ma20: 6.7
- ma60: 6.41
- ma120: 5.97
- return_5d: 0.15
- return_20d: 8.64
- volume_ratio: 0.37
- distance_to_ma20_pct_auxiliary: 1.35
- distance_to_high_60_pct: -18

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,6.25,6.34,6.17,6.32,1479643,6.37,-0.76,6.52,6,0.42
20260811,6.34,6.34,6.13,6.23,1373779,6.36,-2,6.47,6.03,0.46
20260812,6.16,6.23,6.08,6.16,2348831,6.34,-2.85,6.42,6.05,0.86
20260813,6.16,6.21,6.12,6.18,1064961,6.33,-2.32,6.38,6.07,0.42
20260814,6.18,6.23,6.11,6.2,1732758,6.32,-1.84,6.36,6.09,0.74
20260817,6.2,6.3,6.12,6.2,1522049,6.31,-1.69,6.34,6.11,0.68
20260818,6.5,6.82,6.5,6.82,4865868,6.35,7.41,6.34,6.14,2.1
20260819,6.86,7.2,6.5,6.92,12759052,6.4,8.17,6.35,6.17,4.56
20260820,7,7,6.66,6.72,5344338,6.42,4.61,6.36,6.2,1.83
20260821,6.78,7.39,6.76,7.39,12206714,6.5,13.61,6.39,6.24,3.58
20260824,8.03,8.03,7.1,7.22,20912344,6.56,9.99,6.43,6.27,4.8
20260825,7.1,7.43,7.02,7.17,7586016,6.61,8.4,6.47,6.31,1.66
20260826,7.08,7.17,6.88,6.9,6398171,6.64,3.94,6.51,6.32,1.36
20260827,6.86,6.97,6.79,6.86,2319898,6.66,3.05,6.55,6.33,0.49
20260828,6.87,6.87,6.75,6.78,2326754,6.67,1.69,6.58,6.34,0.49
20260831,6.8,6.9,6.76,6.8,1899508,6.68,1.82,6.61,6.35,0.4
20260901,6.81,6.83,6.75,6.76,1727040,6.68,1.12,6.63,6.36,0.36
20260902,6.8,6.83,6.73,6.83,1669108,6.7,1.98,6.65,6.38,0.36
20260903,6.85,6.99,6.74,6.74,2358199,6.7,0.59,6.67,6.39,0.51
20260904,6.69,6.98,6.69,6.79,1738088,6.71,1.22,6.7,6.41,0.37
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 31.63
- over_600_ratio: 29.15
- over_800_ratio: 28.36
- over_1000_ratio: 26.33
- over_400_change_1w: -0.08
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,32.4,0.06,28.67,-0.04,26.74,0.29,1,False,True
20260626,32.35,-0.05,28.75,0.08,26.7,-0.04,2,False,True
20260703,32.46,0.11,28.81,0.06,26.76,0.06,3,True,True
20260709,33.01,0.55,29.54,0.73,27.62,0.86,4,True,True
20260717,31.75,-1.26,28.42,-1.12,26.08,-1.54,0,False,False
20260724,31.63,-0.12,28.38,-0.04,26.36,0.28,1,False,True
20260731,31.84,0.21,28.72,0.34,26.6,0.24,2,True,True
20260807,31.85,0.01,28.63,-0.09,26.72,0.12,3,False,True
20260814,32.01,0.16,28.75,0.12,26.84,0.12,4,True,True
20260821,31.71,-0.3,28.59,-0.16,26.57,-0.27,0,False,False
20260828,31.71,0,28.39,-0.2,26.36,-0.21,0,False,False
20260904,31.63,-0.08,28.36,-0.03,26.33,-0.03,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2601 | 益航 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | continued_overheated | 1.董事會決議日期:115/09/02 2.減資基準日:115/08/21 3.減資換發股票作業計畫: 一、本公司為辦理減資換發股票，依據「臺灣證券交易所股份有限公司營業細則」及    「臺灣證券交易所股份有限公司上市公司換發有價證券作業程序」之規定，訂定本     作業計劃。  二、本次應換發之股票，包含歷年發行之全部股票，計上市普通股824,776,067股，每     股面額為新台幣壹拾元，共計新台幣8,247,760,670元。  三、本次減資新台幣1,343,970,560元，銷除已發行上市股份134,397,056股，用以彌     補虧損及改善財務結構；依公司法第168條之規定，減少資本應依股東所持股份比     例減少之。  四、減資比率：16.2949753%，每仟股換發837.050247股。     (即每仟股減少162.949753股)。  五、減資後換發之普通股股份總數及總金額：     減資後之普通股總股數(股)：690,379,011股，每股面額(元)：10元，減資後之普     通股實收資本總額(元)：6,903,790,110元。  六、本次減資銷除股份換發新股票(全部採無實體發行)，依「減資換股基準日」之股東     名簿記載各股東持有股份分別計算，每仟股換發837.050247股；已存放在證券集保     帳戶之股票，由臺灣集中保管結算所股份有限公司於新股上市買賣日統一換發，股     東不須辦理任何手續換發新股票，換發劃撥集保之股東以畸零股款作為抵繳無實體     劃撥之費用。減資後不足一股之畸零股，股東得於減資換股停止過戶日前五日起至     停止過戶日前一日止向本公司股務代理機構辦理合併拼湊整股之登記，未拼湊或拼     湊後仍不足一股之畸零股，由本公司依「減資換股基準日」前在股票公開集中交易     市場最後交易日之收盤價給付現金予股東，計算至元為止(元以下無條件捨去)，並     授權董事長洽特定人依上述收盤價承購。  七、減資換發股票日程     (一)減資換股基準日訂為民國115年10月03日，並自115年10月05日開始全面換發新         股票(無實體發行)。     (二)減資股票最後過戶日：民國115年09月24日。     (三)為配合上述換股作業，舊股票自民國115年09月23日起至115年10月03日止，停         止在市場買賣交易。     (四)為配合上述換股作業，舊股票自民國115年09月29日起至115年10月03日止，停         止辦理過戶。     (五)普通股新股上市日期訂為民國115年10月05日。自新股票上市之日起原上市買         賣之舊股票不得作為買賣交割之標的。     (六)減資後新股之權利義務與原發行之股份相同。  八、換發程序及手續：     (一)由於本公司已採無實體發行有價證券，屆時將不再印製實體股票，故請尚未在         證券商處開設集保帳戶之股東，儘速至往來證券商開立集保帳戶，以利辦理換         發作業。     (二)辦妥股票過戶但尚未換發全面無實體之股東應備妥下列文件申請換發：         1.舊股票。         2.換發股票申請書(由凱基證券提供)。         3.股東原留印鑑章。         4.證券集保存摺影本，至本公司股務代理機構辦理換發。     (三)尚未辦理股票過戶及尚未換發全面無實體之股東應備妥下列文件同時辦理過戶         及換發手續：         1.舊股票。         2.股票過戶申請書。         3.買進報告書或交易稅完稅證明單或股票領回號碼清單。         4.身分證正反面影本、印鑑章。         5.換發股票申請書。         6.證券集保存摺影本。     (四)原已存放於證券集保帳戶之股票，由臺灣集中保管結算所股份有限公司於新股         新股上市買賣日統一換發為無實體之新股上市買賣，不需辦理任何手續。     (五)換發地點：本公司股務代理機構「凱基證券股份有限公司股務代理部」 (地址         ：臺北市重慶南路一段2號5樓，電話：（02）2389-2999)。  九、其他未盡事宜，擬依公司法及其他相關法令辦理。  十、本計劃書由本公司洽臺灣證券交易所核備後辦理之，本公司將於普通股新股上市日     前分函通知各股東。 4.換發股票基準日:115/10/05 5.停止過戶起始日期:115/09/29 6.停止過戶截止日期:115/10/03 7.減資後新股權利義務:減資後新股之權利義務與原發行之股份相同。 8.新股預計上市日:115/10/05 9.預計減資新股上市後之上市普通股股數:690,379,011股 10.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 11.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，   請說明股權流通性偏低之因應措施:不適用 12.其他應敘明事項:經115/06/18股東會通過減資彌補虧損案，授權董事長依公司法或相 關法令規定全權處理之。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2601 | 益航 | 6 | 6 | 5 | 9 | 15 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
