# INDIVIDUAL STOCK CHATGPT PACKET - 1326 台化

## Metadata
- generated_at: 2026-07-15 22:26:23 Asia/Taipei
- stock_id: 1326
- stock_name: 台化
- packet_status: standard_180d_window_packet
- latest_price_date: 20260715
- price_rows: 304
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1326_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1326_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1326.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1326.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1326.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1326.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1326_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1326_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1326_latest.md?ref=main

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
- date: 20260715
- open: 68.1
- high: 72.4
- low: 67.1
- close: 70.8
- volume: 123945119
- ma5: 65.5
- ema23_primary: 59.83
- distance_to_ema23_pct: 18.34
- ma20: 59.74
- ma60: 52.51
- ma120: 47.7
- return_5d: 11.85
- return_20d: 37.21
- volume_ratio: 1.97
- distance_to_ma20_pct_auxiliary: 18.51
- distance_to_high_60_pct: -3.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260616,52.8,55,51.8,52.1,41063981,49.33,5.61,49.02,48.26,1.17
20260617,52.1,55.2,51.1,53.7,33486429,49.7,8.05,49.48,48.39,0.93
20260618,54.6,55.2,53.7,54.2,31267057,50.07,8.24,49.91,48.58,0.84
20260622,55,57.2,54.1,56.2,33297275,50.58,11.1,50.45,48.8,0.87
20260623,58.5,59.2,53,53.1,52379280,50.79,4.54,50.85,48.97,1.31
20260624,52.5,57.7,51.3,57.7,67367428,51.37,12.33,51.52,49.18,1.58
20260625,58.7,62.3,58.2,59.5,83820012,52.05,14.32,52.22,49.43,1.83
20260626,58.3,58.3,53.8,54.2,46433274,52.23,3.78,52.66,49.52,1
20260629,54.4,55.5,53.1,54.9,17116244,52.45,4.67,52.91,49.69,0.39
20260630,55.6,56.7,54,54.6,22447454,52.63,3.75,52.95,49.84,0.54
20260701,56.1,57.9,55.4,56.3,34830146,52.93,6.36,53.04,50.03,0.9
20260702,55.5,61.9,55.1,61.9,64670626,53.68,15.31,53.31,50.31,1.69
20260703,63,68,62.9,68,97646905,54.87,23.92,53.95,50.69,2.43
20260706,72.8,73,67.2,67.6,129752660,55.93,20.86,54.69,51.05,2.88
20260707,66.8,66.8,63.3,63.3,52450563,56.55,11.94,55.42,51.35,1.14
20260708,63.8,66.4,63.4,64.7,74071252,57.23,13.06,56.24,51.6,1.52
20260709,64.7,64.7,59.4,60,59118264,57.46,4.42,56.93,51.69,1.17
20260713,60,66,60,65,96160170,58.09,11.9,57.87,51.93,1.77
20260714,65.3,67.2,63.8,67,94558841,58.83,13.89,58.78,52.18,1.63
20260715,68.1,72.4,67.1,70.8,123945119,59.83,18.34,59.74,52.51,1.97
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 82.95
- over_600_ratio: 81.88
- over_800_ratio: 81.12
- over_1000_ratio: 80.46
- over_400_change_1w: -0.02
- over_800_change_1w: -0.01
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.26,,80.49,,79.74,,0,False,False
20260508,82.26,0,80.43,-0.06,79.78,0.04,1,False,True
20260515,81.81,-0.45,79.88,-0.55,79.25,-0.53,0,False,False
20260522,81.52,-0.29,79.56,-0.32,78.91,-0.34,0,False,False
20260529,81.33,-0.19,79.46,-0.1,78.74,-0.17,0,False,False
20260605,82.37,1.04,80.47,1.01,79.79,1.05,1,True,True
20260612,81.8,-0.57,79.88,-0.59,79.21,-0.58,0,False,False
20260618,82.4,0.6,80.48,0.6,79.83,0.62,1,True,True
20260626,82.97,0.57,81.13,0.65,80.44,0.61,2,True,True
20260703,82.95,-0.02,81.12,-0.01,80.46,0.02,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 1326 | 台化 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | continued_overheated | 1.事實發生日:115/07/09 2.公司名稱:臺灣化學纖維股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司2026年第二季自結合併損益 6.因應措施:無 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 一、2026年第2季自結合併損益與2026年第1季比較： (一)2026年第2季合併營業額871億5,428萬元，與2026第1季比較增加54億元，成長 6.6％，其中量差減少104.3億元，售價差增加158.3億元。 1.售量方面： (1)台化：減少86.2億元 ARO-3及SM-2廠安排定檢，PX、SM產銷量及萃餘油回售台塑化，合計減少69.5億元； PS、ABS及PP急漲後回跌、市場價格混亂及遠洋運費上漲，影響客戶觀望，銷售減少 15.8億元；苯酚下游客戶停車減產，銷售減少2.3億元。 (2)台化寧波：減少20億元 PS、ABS行情急漲後下跌，市場價格混亂客戶觀望，銷售減少21.7億元；PIA下游客戶 減產，提貨需求降低，影響4.5億元。另PTA第一季因春節影響需求減少，本季下游聚 酯恢復生產，銷售增加6.3億元。 (3)其他子公司： 台灣醋酸適逢下游傳統淡季，銷售減少3億元。另越南FIC發電機組配合國家電網調度 運轉時數，及SPP粒隨行就市拓展銷售，合計增加6.2億元。 2.售價方面： 主要係中東戰事推升原油行情走強，帶動原料及產品價格跟漲，及持續調整產品組合 及推動差異化規格提升價格及利潤。 (二)2026年第2季合併稅前利益70.2億元與2026年第1季比較，減少2.8億元，主要為： 1.營業利益減少12億元： 美伊6月達成和平協議並開放荷姆茲海峽後，原油及石化原料價格走低，部分同業削價 競爭影響市場價格混亂，客戶觀望僅依剛需補貨等因素，影響產品售價承壓下跌，加上 大型機組安排定檢產銷量減少，致營業利益減少。 2.合併營業外淨收益增加9.2億元： (1)現金股利增加8億元，主要塑化增加4.4億元、台塑增加2.4億元。 (2)權益法投資收益增加7.2億元，主要塑化增加4.2億元、麥寮汽電增加3.1億元。 (3)兌盈減少3.5億元(-/本季；3.5億元/上季)。 (三)2026年第2季歸屬母公司稅後利益為60億9,250萬元，每股稅後盈餘1.04元，比2026 年第1季減少0.03元/股。 二、2026年上半年自結合併損益與2025年上半年比較： (一)2026年上半年合併營業額1,689億409萬元，與2025年上半年比較增加164.5億元， 成長10.8％，其中量差減少50.9億元，售價差增加215.4億元。 1.售量方面： (1)台化：減少6.9億元 OX、PTA及PIA下游客戶市況不佳減產，提貨需求降低，銷售減少42億元；PS、ABS及PP 推動精實生產，產銷量減少31.3億元。另PX拓展銷售，增加48.2億元；SM自用減少外售 增加11.6億元；酚酮去年安排定檢，今年產銷正常，增加5.3億元。 (2)台化寧波：減少36.2億元 ABS供應過剩同業削價競爭，減少產銷量控制庫存，影響19.5億元；PTA及PIA下游客戶 減產，提貨需求降低，影響14.1億元；萃餘油產銷調節減少外售2億元。 (3)其他子公司： 福懋減少11.1億元，主要係長纖布終端消費減弱，品牌客戶庫存偏高減少下單所致。 台灣醋酸市況不佳，銷售減少2.2億元。另越南FIC增加5.5億元，主要係SPP粒拓展工 業絲規格並隨行就市爭取訂單，及發電機組配合國家電網調度運轉時數增加。 2.售價方面： 美伊地緣衝突推動原油走強，帶動原料行情上漲及差異化產品比例提高，拉升平均售 價。 (二)2026上半年合併稅前利益143.1億元與2025上半年比較，增加218億元，主要為： 1.營業利益增加80億元： 持續優化產品組合及推動精實生產，因應產品市況，適時調整產銷爭取獲利，加上美 伊戰爭發生後，推升油價及產品售價，擴大與原料成本的獲利價差。 2.營業外淨收益增加138億元： (1)權益法投資收益增加108.8億元，主要塑化增加106億元、福懋科增加2.9億元。 (2)兌損減少26億元(3.4億元/2026上半年；-22.6億元/2025上半年)。 (3)現金股利增加3.4億元，主要今年台塑股利提前發放，增加2.4億元。 (三)2026年上半年歸屬母公司稅後利益為123億3,754萬元，每股稅後盈餘2.11元，比 2025年上半年增加3.35元/股。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 1326 | 台化 | 5 | 2 | 5 | 9 | 16 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 1326 | 台化 | 131 | 9 | 37779100.0 | 127130.0 | 297.17 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
