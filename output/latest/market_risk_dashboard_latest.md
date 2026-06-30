# 市場風險與大盤期權背景

- generated_at: `2026-06-30 14:43:59 Asia/Taipei`
- data_date: `20260630`
- market_regime: `correction`
- risk_level: `very_high_risk`
- risk_score: `7`
- futures_options_source_status: `ready`

## 資料狀態

本報告使用已收錄的官方大盤指數資料，以及期交所期貨、選擇權、Put/Call 與 Taiwan VIX 資料。定位是市場風險背景，不是個股買賣指令。

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260629 |
| futures_contracts | ok | 66 | 20260629 |
| options_call_put | ok | 30 | 20260629 |
| put_call_ratio | ok | 20 | 20260629 |
| taiwan_vix | ok | 82 | 20260629 |

## 大盤指數結構

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 46,125.91 | -2.07% | +1.74% | True | True | mild_bull |
| TPEx | 426.97 | -3.14% | -4.27% | False | True | correction |

## 期貨選擇權部位

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -76,627 | foreign_heavy_net_short |
| Dealer TX futures net OI | +2,415 |  |
| Trust TX futures net OI | +62,962 |  |
| Retail MTX net OI proxy | +1,266 | neutral |
| Foreign TXO call net OI | +9 |  |
| Foreign TXO put net OI | +4,220 |  |
| TXO put/call OI ratio | 123.92% | neutral |
| Taiwan VIX | 39.98 | panic_high |

## 近期總經事件日曆

- 20260625 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 1st Quarter 2026 (days=-5, importance=high)
- 20260625 US_PCE_personal_income: Personal Income and Outlays, May 2026 (days=-5, importance=high)
- 20260702 US_employment_situation: Employment Situation release schedule: June 2026 (days=2, importance=high)
- 20260707 US_trade: U.S. International Trade in Goods and Services, May 2026 (days=7, importance=medium)
- 20260714 US_CPI: CPI release schedule: June 2026 (days=14, importance=high)
- 20260729 FOMC: FOMC decision (July 28-29, 2026) (days=29, importance=high)
- 20260730 US_GDP: GDP (Advance Estimate), 2nd Quarter 2026 (days=30, importance=medium)
- 20260730 US_PCE_personal_income: Personal Income and Outlays, June 2026 (days=30, importance=high)

## 半年技術圖表

PDF 固定納入半年圖表，包含指數趨勢、波動/期權指標、外資台指期部位與散戶小台 proxy。若資料不足，圖表或文字會明確標示限制。

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## 技術與型態重點

- TWSE / TAIEX: mild_bull; close 46,125.91; 6M range 28,707.13-47,741.51; distance from 6M high -3.38%; above MA20=True, above MA60=True.
- TPEx / OTC: correction; close 426.97; 6M range 274.54-453.50; distance from 6M high -5.85%; above MA20=False, above MA60=True.

## 散戶小台 proxy

- 這是反向情緒輔助指標，以三大法人小台淨未平倉的反向 proxy 估算。
- latest_proxy_value: `+1,266`
- state: `neutral`
- proxy 為正代表非三大法人帳戶偏多；擁擠偏多只能視為追高風險，不是單獨放空訊號。
- proxy 為負代表非三大法人帳戶偏空；極端偏空可列反彈觀察，但仍需指數與廣度確認。

## 風險提醒

- TPEx correction
- Taiwan VIX panic-high
- Foreign TX futures heavy net short

## 使用邊界

- 本報告用於判斷大盤風險、台指期背景與部位曝險節奏。
- 不可把單一 VIX、Put/Call、外資期貨或散戶小台指標當成買賣訊號。
- 每日全市場候選股可引用大盤背景，但個股是否入選仍以各模型條件為準。

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `39.98`
- 252D high / low / percentile: `44.01` / `25.68` / `91.58%`
- 504D percentile: `-`
- z-score: `1.13`
- vix_return_5d / 10d / 20d: `5.68%` / `-4.72%` / `11.46%`
- TWSE / TPEx position: TWSE dist 60D high `-3.38%`, TPEx dist 60D high `-5.85%`
- vix_index_interpretation: `vix_context_neutral_observe`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `1,266`
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
