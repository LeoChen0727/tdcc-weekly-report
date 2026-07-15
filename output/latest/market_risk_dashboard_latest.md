# 市場風險與大盤期權背景

- generated_at: `2026-07-15 12:47:19 Asia/Taipei`
- data_date: `20260714`
- market_regime: `high_risk`
- risk_level: `very_high_risk`
- risk_score: `10`
- futures_options_source_status: `ready`

## 資料狀態

本報告使用已收錄的官方大盤指數資料，以及期交所期貨、選擇權、Put/Call 與 Taiwan VIX 資料。定位是市場風險背景，不是個股買賣指令。

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260714 |
| futures_contracts | ok | 66 | 20260714 |
| options_call_put | ok | 30 | 20260714 |
| put_call_ratio | ok | 20 | 20260714 |
| taiwan_vix | ok | 70 | 20260714 |

## 大盤指數結構

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 44,737.95 | -3.91% | +1.29% | False | True | correction |
| TPEx | 407.41 | -7.36% | -2.93% | False | False | high_risk |

## 期貨選擇權部位

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -83,390 | foreign_heavy_net_short |
| Dealer TX futures net OI | +2,352 |  |
| Trust TX futures net OI | +73,873 |  |
| Retail MTX net OI proxy | +6,888 | neutral |
| Foreign TXO call net OI | +2,333 |  |
| Foreign TXO put net OI | +13,201 |  |
| TXO put/call OI ratio | 99.31% | neutral |
| Taiwan VIX | 36.61 | panic_high |

## 近期總經事件日曆

- 20260714 US_CPI: CPI release schedule: June 2026 (days=-1, importance=high)
- 20260716 US_PCE_personal_income: Prototype Distribution of State Personal Income, 2024 (days=1, importance=high)
- 20260729 FOMC: FOMC decision (July 28-29, 2026) (days=14, importance=high)
- 20260730 US_GDP: GDP (Advance Estimate), 2nd Quarter 2026 (days=15, importance=medium)
- 20260730 US_PCE_personal_income: Personal Income and Outlays, June 2026 (days=15, importance=high)
- 20260804 US_trade: U.S. International Trade in Goods and Services, June 2026 (days=20, importance=medium)
- 20260807 US_employment_situation: Employment Situation release schedule: July 2026 (days=23, importance=high)
- 20260812 US_CPI: CPI release schedule: July 2026 (days=28, importance=high)

## 半年技術圖表

PDF 固定納入半年圖表，包含指數趨勢、波動/期權指標、外資台指期部位與散戶小台 proxy。若資料不足，圖表或文字會明確標示限制。

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## 技術與型態重點

- TWSE / TAIEX: correction; close 44,737.95; 6M range 30,810.58-47,741.51; distance from 6M high -6.29%; above MA20=False, above MA60=True.
- TPEx / OTC: high_risk; close 407.41; 6M range 288.96-453.50; distance from 6M high -10.16%; above MA20=False, above MA60=False.

## 散戶小台 proxy

- 這是反向情緒輔助指標，以三大法人小台淨未平倉的反向 proxy 估算。
- latest_proxy_value: `+6,888`
- state: `neutral`
- proxy 為正代表非三大法人帳戶偏多；擁擠偏多只能視為追高風險，不是單獨放空訊號。
- proxy 為負代表非三大法人帳戶偏空；極端偏空可列反彈觀察，但仍需指數與廣度確認。

## 風險提醒

- TWSE correction
- TPEx below MA60 and 20d return negative
- Taiwan VIX panic-high
- Foreign TX futures heavy net short

## 使用邊界

- 本報告用於判斷大盤風險、台指期背景與部位曝險節奏。
- 不可把單一 VIX、Put/Call、外資期貨或散戶小台指標當成買賣訊號。
- 每日全市場候選股可引用大盤背景，但個股是否入選仍以各模型條件為準。

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `36.61`
- 252D high / low / percentile: `44.01` / `25.68` / `56.73%`
- 504D percentile: `-`
- z-score: `0.34`
- vix_return_5d / 10d / 20d: `-0.76%` / `-8.43%` / `-12.75%`
- TWSE / TPEx position: TWSE dist 60D high `-6.29%`, TPEx dist 60D high `-10.16%`
- vix_index_interpretation: `vix_context_neutral_observe`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `6,888`
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
