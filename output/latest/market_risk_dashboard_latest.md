# 市場風險與大盤期權背景

- generated_at: `2026-06-24 19:50:01 Asia/Taipei`
- data_date: `20260624`
- market_regime: `mild_bull`
- risk_level: `high_risk`
- risk_score: `4`
- futures_options_source_status: `ready`

## 資料狀態

本報告使用已收錄的官方大盤指數資料，以及期交所期貨、選擇權、Put/Call 與 Taiwan VIX 資料。定位是市場風險背景，不是個股買賣指令。

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260624 |
| futures_contracts | ok | 66 | 20260624 |
| options_call_put | ok | 30 | 20260624 |
| put_call_ratio | ok | 22 | 20260624 |
| taiwan_vix | ok | 79 | 20260624 |

## 大盤指數結構

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 47,100.65 | +3.75% | +7.92% | True | True | strong_bull |
| TPEx | 442.09 | +2.75% | +0.64% | True | True | mild_bull |

## 期貨選擇權部位

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -83,605 | foreign_heavy_net_short |
| Dealer TX futures net OI | +3,277 |  |
| Trust TX futures net OI | +60,757 |  |
| Retail MTX net OI proxy | +8,469 | neutral |
| Foreign TXO call net OI | -765 |  |
| Foreign TXO put net OI | +3,981 |  |
| TXO put/call OI ratio | 134.59% | neutral |
| Taiwan VIX | 40.92 | panic_high |

## 近期總經事件日曆

- 20260617 FOMC: FOMC decision (June 16-17, 2026) (days=-7, importance=high)
- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=1, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=1, importance=high)
- 20260702 US_employment_situation: Employment Situation release schedule: June 2026 (days=8, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=13, importance=medium)
- 20260714 US_CPI: CPI release schedule: June 2026 (days=20, importance=high)
- 20260729 FOMC: FOMC decision (July 28-29, 2026) (days=35, importance=high)
- 20260730 US_GDP: GDP (Advance Estimate), 2nd Quarter 2026 (days=36, importance=medium)

## 半年技術圖表

PDF 固定納入半年圖表，包含指數趨勢、波動/期權指標、外資台指期部位與散戶小台 proxy。若資料不足，圖表或文字會明確標示限制。

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## 技術與型態重點

- TWSE / TAIEX: strong_bull; close 47,100.65; 6M range 28,371.98-47,741.51; distance from 6M high -1.34%; above MA20=True, above MA60=True.
- TPEx / OTC: mild_bull; close 442.09; 6M range 269.75-453.50; distance from 6M high -2.52%; above MA20=True, above MA60=True.

## 散戶小台 proxy

- 這是反向情緒輔助指標，以三大法人小台淨未平倉的反向 proxy 估算。
- latest_proxy_value: `+8,469`
- state: `neutral`
- proxy 為正代表非三大法人帳戶偏多；擁擠偏多只能視為追高風險，不是單獨放空訊號。
- proxy 為負代表非三大法人帳戶偏空；極端偏空可列反彈觀察，但仍需指數與廣度確認。

## 風險提醒

- TWSE strong bull
- Taiwan VIX panic-high
- Foreign TX futures heavy net short

## 使用邊界

- 本報告用於判斷大盤風險、台指期背景與部位曝險節奏。
- 不可把單一 VIX、Put/Call、外資期貨或散戶小台指標當成買賣訊號。
- 每日全市場候選股可引用大盤背景，但個股是否入選仍以各模型條件為準。

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `40.92`
- 252D high / low / percentile: `43.92` / `25.68` / `94.51%`
- 504D percentile: `-`
- z-score: `1.43`
- vix_return_5d / 10d / 20d: `4.33%` / `5.87%` / `24.34%`
- TWSE / TPEx position: TWSE dist 60D high `-1.34%`, TPEx dist 60D high `-2.52%`
- vix_index_interpretation: `index_strong_but_hedging_elevated`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `8,469`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low / percentile: `-` / `-` / `-`
- 504D percentile: `-`
- retail_mtx_index_interpretation: `insufficient_history_observe_only`

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `insufficient_history_observe_only`
- sentiment_warning_level: `insufficient`
- data_quality_note: 資料不足 / 僅能觀察：VIX 或散戶小台歷史樣本未達 60 筆，不能判斷是否達歷史極端。

Operation meaning: use sentiment context only with TWSE / TPEx technical position, market_regime, Put/Call, and foreign TX futures net OI. Do not use VIX or retail MTX as standalone buy/sell signals.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
