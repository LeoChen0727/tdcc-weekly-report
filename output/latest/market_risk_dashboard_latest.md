# 市場風險與大盤期權背景

- generated_at: `2026-10-28 19:49:00 Asia/Taipei`
- data_date: `20261028`
- market_regime: `high_risk`
- risk_level: `very_high_risk`
- risk_score: `7`
- futures_options_source_status: `ready`

## 資料狀態

本報告使用已收錄的官方大盤指數資料，以及期交所期貨、選擇權、Put/Call 與 Taiwan VIX 資料。定位是市場風險背景，不是個股買賣指令。

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20261028 |
| futures_contracts | ok | 66 | 20261028 |
| options_call_put | ok | 30 | 20261028 |
| put_call_ratio | ok | 19 | 20261028 |
| taiwan_vix | ok | 80 | 20261028 |

## 大盤指數結構

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 47,035.58 | +0.46% | -2.33% | False | True | correction |
| TPEx | 394.61 | +0.14% | -4.63% | False | False | high_risk |

## 期貨選擇權部位

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -84,917 | foreign_heavy_net_short |
| Dealer TX futures net OI | +483 |  |
| Trust TX futures net OI | +87,179 |  |
| Retail MTX net OI proxy | +8,575 | neutral |
| Foreign TXO call net OI | +675 |  |
| Foreign TXO put net OI | +896 |  |
| TXO put/call OI ratio | 69.38% | call_crowded_or_low_hedge |
| Taiwan VIX | 27.42 | watch |

## 近期總經事件日曆

- 20261028 FOMC: FOMC decision (October 27-28, 2026) (days=0, importance=high)
- 20261029 US_GDP: GDP (Advance Estimate), 3rd Quarter 2026 (days=1, importance=medium)
- 20261029 US_PCE_personal_income: Personal Income and Outlays, September 2026 (days=1, importance=high)
- 20261104 US_trade: U.S. International Trade in Goods and Services, September 2026 (days=7, importance=medium)
- 20261106 US_employment_situation: Employment Situation release schedule: BY MONTH FEBRUARY 2026 MARCH 2026 APRIL 2026 MAY 2026 JUNE 2026 JULY 2026 AUGUST 2026 SEPTEMBER 2026 OCTOBER 2026 NOVEMBER 2026 DECEMBER 2026 JANUARY 2027 FEBRUARY 2027 MARCH 2027 APRIL 2027 MAY 2027 JUNE 2027 JULY 2027 AUGUST 2027 SEPTEMBER 2027 OCTOBER 2027 NOVEMBER 2027 DECEMBER 2027 ENTIRE YEAR, 2026 ENTIRE YEAR, 2027 PRIOR YEARS BY NEWS RELEASE BUSINESS EMPLOYMENT DYNAMICS CONSUMER PRICE INDEX COUNTY EMPLOYMENT AND WAGES EMPLOYMENT COST INDEX EMPLOYMENT SITUATION JOB OPENINGS AND LABOR TURNOVER PRODUCER PRICE INDEX PRODUCTIVITY AND COSTS REAL EARNINGS U.S. EXPORT AND IMPORT PRICE INDEXES METROPOLITAN AREA EMPLOYMENT AND UNEMPLOYMENT STATE EMPLOYMENT AND UNEMPLOYMENT (days=9, importance=high)
- 20261106 US_employment_situation: Employment Situation release schedule: October 2026 (days=9, importance=high)
- 20261110 US_CPI: CPI release schedule: BY MONTH FEBRUARY 2026 MARCH 2026 APRIL 2026 MAY 2026 JUNE 2026 JULY 2026 AUGUST 2026 SEPTEMBER 2026 OCTOBER 2026 NOVEMBER 2026 DECEMBER 2026 JANUARY 2027 FEBRUARY 2027 MARCH 2027 APRIL 2027 MAY 2027 JUNE 2027 JULY 2027 AUGUST 2027 SEPTEMBER 2027 OCTOBER 2027 NOVEMBER 2027 DECEMBER 2027 ENTIRE YEAR, 2026 ENTIRE YEAR, 2027 PRIOR YEARS BY NEWS RELEASE BUSINESS EMPLOYMENT DYNAMICS CONSUMER PRICE INDEX COUNTY EMPLOYMENT AND WAGES EMPLOYMENT COST INDEX EMPLOYMENT SITUATION JOB OPENINGS AND LABOR TURNOVER PRODUCER PRICE INDEX PRODUCTIVITY AND COSTS REAL EARNINGS U.S. EXPORT AND IMPORT PRICE INDEXES METROPOLITAN AREA EMPLOYMENT AND UNEMPLOYMENT STATE EMPLOYMENT AND UNEMPLOYMENT (days=13, importance=high)
- 20261110 US_CPI: CPI release schedule: October 2026 (days=13, importance=high)

## 半年技術圖表

PDF 固定納入半年圖表，包含指數趨勢、波動/期權指標、外資台指期部位與散戶小台 proxy。若資料不足，圖表或文字會明確標示限制。

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## 技術與型態重點

- TWSE / TAIEX: correction; close 47,035.58; 6M range 38,926.63-49,822.55; distance from 6M high -5.59%; above MA20=False, above MA60=True.
- TPEx / OTC: high_risk; close 394.61; 6M range 326.23-453.50; distance from 6M high -12.99%; above MA20=False, above MA60=False.

## 散戶小台 proxy

- 這是反向情緒輔助指標，以三大法人小台淨未平倉的反向 proxy 估算。
- latest_proxy_value: `+8,575`
- state: `neutral`
- proxy 為正代表非三大法人帳戶偏多；擁擠偏多只能視為追高風險，不是單獨放空訊號。
- proxy 為負代表非三大法人帳戶偏空；極端偏空可列反彈觀察，但仍需指數與廣度確認。

## 風險提醒

- TWSE correction
- TPEx below MA60 and 20d return negative
- Foreign TX futures heavy net short

## 使用邊界

- 本報告用於判斷大盤風險、台指期背景與部位曝險節奏。
- 不可把單一 VIX、Put/Call、外資期貨或散戶小台指標當成買賣訊號。
- 每日全市場候選股可引用大盤背景，但個股是否入選仍以各模型條件為準。

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `27.42`
- 252D high / low / percentile: `44.33` / `21.18` / `21.14%`
- 504D percentile: `-`
- z-score: `-0.97`
- vix_return_5d / 10d / 20d: `-7.68%` / `8.98%` / `25.61%`
- TWSE / TPEx position: TWSE dist 60D high `-5.59%`, TPEx dist 60D high `-8.76%`
- vix_index_interpretation: `vix_context_neutral_observe`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `8,575`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low / percentile: `16,227` / `-3,246` / `64.84%`
- 504D percentile: `-`
- retail_mtx_index_interpretation: `retail_positioning_normal`

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `low`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

Operation meaning: use sentiment context only with TWSE / TPEx technical position, market_regime, Put/Call, and foreign TX futures net OI. Do not use VIX or retail MTX as standalone buy/sell signals.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
