# 市場風險與大盤期權背景

- generated_at: `2026-09-03 02:46:41 Asia/Taipei`
- data_date: `20260902`
- market_regime: `mild_bull`
- risk_level: `neutral`
- risk_score: `1`
- futures_options_source_status: `ready`

## 資料狀態

本報告使用已收錄的官方大盤指數資料，以及期交所期貨、選擇權、Put/Call 與 Taiwan VIX 資料。定位是市場風險背景，不是個股買賣指令。

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260902 |
| futures_contracts | ok | 66 | 20260902 |
| options_call_put | ok | 30 | 20260902 |
| put_call_ratio | ok | 23 | 20260902 |
| taiwan_vix | ok | 66 | 20260902 |

## 大盤指數結構

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 46,164.72 | +0.72% | +3.48% | True | True | mild_bull |
| TPEx | 406.96 | +2.86% | +6.05% | True | True | strong_bull |

## 期貨選擇權部位

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -85,329 | foreign_heavy_net_short |
| Dealer TX futures net OI | +1,109 |  |
| Trust TX futures net OI | +75,062 |  |
| Retail MTX net OI proxy | +3,882 | neutral |
| Foreign TXO call net OI | -3,692 |  |
| Foreign TXO put net OI | +26 |  |
| TXO put/call OI ratio | 83.90% | call_crowded_or_low_hedge |
| Taiwan VIX | 26.09 | watch |

## 近期總經事件日曆

- 20260903 US_trade: U.S. International Trade in Goods and Services, July 2026 (days=0, importance=medium)
- 20260904 US_employment_situation: Employment Situation release schedule: August 2026 (days=1, importance=high)
- 20260911 US_CPI: CPI release schedule: August 2026 (days=8, importance=high)
- 20260916 FOMC: FOMC decision (September 15-16, 2026) (days=13, importance=high)
- 20260930 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 2nd Quarter 2026; State PCE, 2025 (days=27, importance=high)
- 20260930 US_PCE_personal_income: Personal Income and Outlays, August 2026 (days=27, importance=high)
- 20261002 US_employment_situation: Employment Situation release schedule: September 2026 (days=29, importance=high)
- 20261006 US_trade: U.S. International Trade in Goods and Services, August 2026 (days=33, importance=medium)

## 半年技術圖表

PDF 固定納入半年圖表，包含指數趨勢、波動/期權指標、外資台指期部位與散戶小台 proxy。若資料不足，圖表或文字會明確標示限制。

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## 技術與型態重點

- TWSE / TAIEX: mild_bull; close 46,164.72; 6M range 31,722.99-47,741.51; distance from 6M high -3.30%; above MA20=True, above MA60=True.
- TPEx / OTC: strong_bull; close 406.96; 6M range 288.96-453.50; distance from 6M high -10.26%; above MA20=True, above MA60=True.

## 散戶小台 proxy

- 這是反向情緒輔助指標，以三大法人小台淨未平倉的反向 proxy 估算。
- latest_proxy_value: `+3,882`
- state: `neutral`
- proxy 為正代表非三大法人帳戶偏多；擁擠偏多只能視為追高風險，不是單獨放空訊號。
- proxy 為負代表非三大法人帳戶偏空；極端偏空可列反彈觀察，但仍需指數與廣度確認。

## 風險提醒

- TPEx strong bull
- Foreign TX futures heavy net short

## 使用邊界

- 本報告用於判斷大盤風險、台指期背景與部位曝險節奏。
- 不可把單一 VIX、Put/Call、外資期貨或散戶小台指標當成買賣訊號。
- 每日全市場候選股可引用大盤背景，但個股是否入選仍以各模型條件為準。

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `26.09`
- 252D high / low / percentile: `44.33` / `24.46` / `3.57%`
- 504D percentile: `-`
- z-score: `-1.89`
- vix_return_5d / 10d / 20d: `-9.03%` / `-15.37%` / `-26.24%`
- TWSE / TPEx position: TWSE dist 60D high `-3.3%`, TPEx dist 60D high `-10.26%`
- vix_index_interpretation: `vix_context_neutral_observe`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `3,882`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low / percentile: `16,227` / `-1,332` / `13.24%`
- 504D percentile: `-`
- retail_mtx_index_interpretation: `retail_positioning_observe`

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `low`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

Operation meaning: use sentiment context only with TWSE / TPEx technical position, market_regime, Put/Call, and foreign TX futures net OI. Do not use VIX or retail MTX as standalone buy/sell signals.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
