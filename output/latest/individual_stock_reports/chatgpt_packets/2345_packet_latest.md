# INDIVIDUAL STOCK CHATGPT PACKET - 2345 智邦

## Metadata
- generated_at: 2026-09-26 22:16:17 Asia/Taipei
- stock_id: 2345
- stock_name: 智邦
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2345_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2345_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2345_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2345_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2345_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2345_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2345_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2345_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2345_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2345_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2345_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2345_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2345.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2345.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2345.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2345.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2345_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2345_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2345_latest.md?ref=main

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
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260924
- open: 1880
- high: 1905
- low: 1855
- close: 1895
- volume: 2611500
- ma5: 1879
- ema23_primary: 1967.22
- distance_to_ema23_pct: -3.67
- ma20: 1968.25
- ma60: 2157.25
- ma120: 2246.33
- return_5d: 5.28
- return_20d: -9.33
- volume_ratio: 0.71
- distance_to_ma20_pct_auxiliary: -3.72
- distance_to_high_60_pct: -32.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,2120,2195,2100,2125,2374655,2167.79,-1.97,2195,2310.08,0.76
20260831,2085,2085,1950,2035,4484579,2156.73,-5.64,2180,2302.17,1.41
20260901,2085,2235,2050,2205,5313838,2160.75,2.05,2174.25,2297.42,1.65
20260902,2145,2205,2105,2140,3470248,2159.02,-0.88,2162,2292.75,1.07
20260903,2150,2165,2060,2090,2730824,2153.27,-2.94,2146,2286.33,0.86
20260904,2145,2190,2075,2100,2163787,2148.83,-2.27,2140.25,2281.92,0.7
20260907,2150,2155,2090,2100,2076808,2144.76,-2.09,2137,2279,0.68
20260908,2130,2140,1950,1955,6441295,2128.95,-8.17,2128,2272.67,2.03
20260909,1960,2070,1960,2015,4715389,2119.45,-4.93,2118,2265.75,1.44
20260910,1990,2005,1955,1965,2982489,2106.58,-6.72,2102.75,2256.5,0.91
20260911,1910,1925,1870,1885,4090126,2088.12,-9.73,2082,2246.33,1.24
20260914,1840,1895,1830,1875,3068576,2070.36,-9.44,2061.25,2237,0.92
20260915,1870,1895,1830,1840,2272078,2051.16,-10.29,2042,2224.42,0.69
20260916,1840,1860,1830,1840,3116998,2033.56,-9.52,2027.75,2214.5,0.96
20260917,1865,1885,1790,1800,4448162,2014.1,-10.63,2012.5,2204.92,1.33
20260918,1810,1855,1810,1855,5848473,2000.84,-7.29,2003.5,2196.17,1.67
20260921,1840,1880,1810,1840,3499481,1987.44,-7.42,1992,2187.17,0.97
20260922,1900,1935,1865,1915,3976822,1981.4,-3.35,1986.25,2180.08,1.09
20260923,1935,1955,1845,1890,4143392,1973.78,-4.24,1978,2170,1.12
20260924,1880,1905,1855,1895,2611500,1967.22,-3.67,1968.25,2157.25,0.71
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 70.31
- over_600_ratio: 65.43
- over_800_ratio: 60.68
- over_1000_ratio: 56.42
- over_400_change_1w: 0.06
- over_800_change_1w: 0.13
- over_1000_change_1w: 0.08
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,71.19,-0.26,61.12,0.13,57.2,0.18,6,False,True
20260717,71.09,-0.1,60.99,-0.13,57.23,0.03,7,False,True
20260724,71.37,0.28,60.99,0,57.25,0.02,8,False,True
20260731,71.41,0.04,61.29,0.3,57.51,0.26,9,False,True
20260807,71.06,-0.35,61.02,-0.27,57.09,-0.42,0,False,False
20260814,71.02,-0.04,60.68,-0.34,56.74,-0.35,0,False,False
20260821,71.25,0.23,61.18,0.5,57.09,0.35,1,True,True
20260828,70.87,-0.38,61.08,-0.1,57.05,-0.04,0,False,False
20260904,71.13,0.26,60.85,-0.23,56.64,-0.41,1,False,False
20260911,70.61,-0.52,60.7,-0.15,56.6,-0.04,0,False,False
20260918,70.25,-0.36,60.55,-0.15,56.34,-0.26,1,False,False
20260924,70.31,0.06,60.68,0.13,56.42,0.08,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2345 | 智邦 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: (1)摩根環球短債基金 (2)摩根美元浮動貨幣基金USD (3)GFUSA/富達基金-美元現金基金 2.事實發生日:115/9/16~115/9/16 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:依公司核決權限辦理 民國115年09月16日 5.交易數量、每單位價格及交易總金額: (1)摩根環球短債基金 交易數量:344仟單位 每單位價格: 約13.34，實際交易淨值以交易對帳單為主 交易總金額: 約USD 4,600,000，實際交易總金額以交易對帳單為主  (2)摩根美元浮動貨幣基金USD 交易數量: 82仟單位 每單位價格: 約125.65，實際交易淨值以交易對帳單為主 交易總金額:約USD 10,400,000，實際交易總金額以交易對帳單為主  (3)GFUSA/富達基金-美元現金基金 交易數量: 1,892仟單位 每單位價格: 約13.5589，實際交易淨值以交易對帳單為主 交易總金額:約USD 25,600,000，實際交易總金額以交易對帳單為主 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人：摩根投信 凱基證券 與公司之關係：無 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 處分利益初估金額約美金1佰萬元 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 一次付清 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依公司核決權限辦理 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 無 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 占總資產比例：5.19 % 占業主權益比例：11.67 % 營運資金數額：新台幣37,876,521仟元 16.經紀人及經紀費用: 無 17.取得或處分之具體目的或用途: 基金贖回 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用,原因：依公司核決權限辦理 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用 23.會計師姓名: 不適用 24.會計師開業證書字號: 不適用 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 2345 | 智邦 | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 38 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: (1)摩根環球短債基金 (2)摩根美元浮動貨幣基金USD (3)GFUSA/富達基金-美元現金基金 2.事實發生日:115/9/16~115/9/16 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:依公司核決權限辦理 民國115年09月16日 5.交易數量、每單位價格及交易總金額: (1)摩根環球短債基金 交易數量:344仟單位 每單位價格: 約13.34，實際交易淨值以交易對帳單為主 交易總金額: 約USD 4,600,000，實際交易總金額以交易對帳單為主  (2)摩根美元浮動貨幣基金USD 交易數量: 82仟單位 每單位價格: 約125.65，實際交易淨值以交易對帳單為主 交易總金額:約USD 10,400,000，實際交易總金額以交易對帳單為主  (3)GFUSA/富達基金-美元現金基金 交易數量: 1,892仟單位 每單位價格: 約13.5589，實際交易淨值以交易對帳單為主 交易總金額:約USD 25,600,000，實際交易總金額以交易對帳單為主 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人：摩根投信 凱基證券 與公司之關係：無 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 處分利益初估金額約美金1佰萬元 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 一次付清 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依公司核決權限辦理 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 無 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 占總資產比例：5.19 % 占業主權益比例：11.67 % 營運資金數額：新台幣37,876,521仟元 16.經紀人及經紀費用: 無 17.取得或處分之具體目的或用途: 基金贖回 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用,原因：依公司核決權限辦理 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用 23.會計師姓名: 不適用 24.會計師開業證書字號: 不適用 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2345 | 智邦 | 10 | 10 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2345 | 智邦 | 318 | 25 | 22910290.0 | 628940.0 | 36.43 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
