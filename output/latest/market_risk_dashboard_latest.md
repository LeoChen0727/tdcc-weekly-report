# 市場風險與大盤期權背景

- generated_at: `2026-09-24 19:49:17 Asia/Taipei`
- data_date: `20260924`
- market_regime: `mild_bull`
- risk_level: `elevated_risk`
- risk_score: `2`
- futures_options_source_status: `ready`

## 資料狀態

本報告使用已收錄的官方大盤指數資料，以及期交所期貨、選擇權、Put/Call 與 Taiwan VIX 資料。定位是市場風險背景，不是個股買賣指令。

| source | status | rows | latest_date |
| --- | --- | ---: | --- |
| institutional_fo | ok | 3 | 20260924 |
| futures_contracts | ok | 66 | 20260924 |
| options_call_put | ok | 30 | 20260924 |
| put_call_ratio | ok | 23 | 20260924 |
| taiwan_vix | ok | 82 | 20260924 |

## 大盤指數結構

| index | close | 5d | 20d | MA20 | MA60 | regime |
| --- | --- | --- | --- | --- | --- | --- |
| TWSE | 48,024.60 | +3.75% | +4.46% | True | True | mild_bull |
| TPEx | 412.99 | +3.72% | +3.15% | True | True | mild_bull |

## 期貨選擇權部位

| indicator | value | state |
| --- | --- | --- |
| Foreign TX futures net OI | -77,031 | foreign_heavy_net_short |
| Dealer TX futures net OI | -1,520 |  |
| Trust TX futures net OI | +72,864 |  |
| Retail MTX net OI proxy | +7,415 | neutral |
| Foreign TXO call net OI | -1,698 |  |
| Foreign TXO put net OI | +1,645 |  |
| TXO put/call OI ratio | 85.33% | neutral |
| Taiwan VIX | 23.12 | watch |

## 近期總經事件日曆

- 20260930 US_PCE_personal_income: GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 2nd Quarter 2026; State PCE, 2025 (days=6, importance=high)
- 20260930 US_PCE_personal_income: Personal Income and Outlays, August 2026 (days=6, importance=high)
- 20261002 US_employment_situation: Employment Situation release schedule: September 2026 (days=8, importance=high)
- 20261006 US_trade: U.S. International Trade in Goods and Services, August 2026 (days=12, importance=medium)
- 20261014 US_CPI: CPI release schedule: September 2026 (days=20, importance=high)
- 20261028 FOMC: FOMC decision (October 27-28, 2026) (days=34, importance=high)
- 20261029 US_GDP: GDP (Advance Estimate), 3rd Quarter 2026 (days=35, importance=medium)
- 20261029 US_PCE_personal_income: Personal Income and Outlays, September 2026 (days=35, importance=high)

## 半年技術圖表

PDF 固定納入半年圖表，包含指數趨勢、波動/期權指標、外資台指期部位與散戶小台 proxy。若資料不足，圖表或文字會明確標示限制。

Index chart data status: TWSE / TAIEX: standard OHLC K-line data is available with volume/turnover overlay. TPEx / OTC: standard OHLC K-line data is available with volume/turnover overlay.

- chart: `output/latest/charts/market_regime/market_index_technical_6m.png`
- chart: `output/latest/charts/market_regime/risk_indicators_6m.png`
- chart: `output/latest/charts/market_regime/foreign_futures_net_oi_6m.png`
- chart: `output/latest/charts/market_regime/retail_mtx_proxy_6m.png`

## 技術與型態重點

- TWSE / TAIEX: mild_bull; close 48,024.60; 6M range 31,722.99-48,157.29; distance from 6M high -0.28%; above MA20=True, above MA60=True.
- TPEx / OTC: mild_bull; close 412.99; 6M range 307.73-453.50; distance from 6M high -8.93%; above MA20=True, above MA60=True.

## 散戶小台 proxy

- 這是反向情緒輔助指標，以三大法人小台淨未平倉的反向 proxy 估算。
- latest_proxy_value: `+7,415`
- state: `neutral`
- proxy 為正代表非三大法人帳戶偏多；擁擠偏多只能視為追高風險，不是單獨放空訊號。
- proxy 為負代表非三大法人帳戶偏空；極端偏空可列反彈觀察，但仍需指數與廣度確認。

## 風險提醒

- Foreign TX futures heavy net short

## 使用邊界

- 本報告用於判斷大盤風險、台指期背景與部位曝險節奏。
- 不可把單一 VIX、Put/Call、外資期貨或散戶小台指標當成買賣訊號。
- 每日全市場候選股可引用大盤背景，但個股是否入選仍以各模型條件為準。

<!-- MARKET_SENTIMENT_CONTEXT_START -->
## VIX Historical Context

- Taiwan VIX latest: `23.12`
- 252D high / low / percentile: `44.33` / `21.18` / `3.21%`
- 504D percentile: `-`
- z-score: `-1.98`
- vix_return_5d / 10d / 20d: `-3.87%` / `-12.02%` / `-14.69%`
- TWSE / TPEx position: TWSE dist 60D high `-0.28%`, TPEx dist 60D high `-7.27%`
- vix_index_interpretation: `low_vol_complacency_at_high`

## Retail MTX Historical Context

- retail_mtx_net_oi_proxy latest: `7,415`
- proxy method: `negative_sum_of_three_institution_mtx_net_oi`
- 252D high / low / percentile: `16,227` / `-3,246` / `54.88%`
- 504D percentile: `-`
- retail_mtx_index_interpretation: `retail_positioning_normal`

## Combined Sentiment Interpretation

- combined_sentiment_interpretation: `sentiment_mixed_observe`
- sentiment_warning_level: `low`
- data_quality_note: short_history：可提供短樣本分位，但未達 252 日完整歷史。

Operation meaning: use sentiment context only with TWSE / TPEx technical position, market_regime, Put/Call, and foreign TX futures net OI. Do not use VIX or retail MTX as standalone buy/sell signals.
<!-- MARKET_SENTIMENT_CONTEXT_END -->
