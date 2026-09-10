# TDCC 潛伏吸籌：有收據全市場研究重建 v1

這是 research-only 的現行固定研究語義歷史重建，不是完整原始 PIT、正式 production selector、正式可採用勝率或已核實 total-return。

formal_use=False；promotion_evidence_allowed=False；full_period_pit_complete=False。

訊號範圍：20260615–20260909；結果資料 as_of：20260909。
有收據日期 40；實際特徵列 78124；支持特徵列 60649；訊號 30123。
價格 proxy 交易列 39462（每部位三種成本情境）；strict 已核實總報酬部位 0。
異常候選 383；未解異常保留 primary，排除版本僅 sensitivity，不是 corrected performance。

## 邊界

- 母體是當日四位且非零開頭的原始行情代碼，包含已註記的可能 91 開頭 TDR；不是今日存活名單，也不是已逐檔驗證普通股分類。
- 只用各日收據指定同一 Git tree 的歷史資料。缺 receipt 日期不產生特徵，不借用 latest；事後結果來源不能補 decision features。
- 每股至少 21 個既有觀測、末 20 個觀測量均值與四批 TDCC；缺交易日揭露、不前填，不把暖身日期或較長少數股票覆蓋冒稱全市場可評估日期。
- 固定研究 v2 enum fallback：phase/status 明確留白；不是正式 production phase classifier。
- 收據支持版本可得時間，但 unknown source lineage 不等於 PIT proof；空白 source 不自行增加模型 gate。
- 買入為下一 session open，D+5/10/20 future close；各持有期獨立持倉鎖，當日出場不接受同股再入場訊號。
- 未調整原始價格 proxy 不套用未證實公司行動現金流／股數變動；不是已核實 total-return、券商成交或模型升級證據。
- 完整官方 calendar event coverage 與 corporate-action coverage 未核實，strict ledger 保持阻擋／未解狀態；proxy 出場不能解除 strict 持倉鎖。
- 不以數值幅度判定資料錯誤。unresolved_anomaly_candidate 保留 primary；正式採用結論仍受阻。
- 不使用月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利、季度及年度財報均不在範圍。

## 主要數值（10 bps，含未解異常候選）

| 持有期 | 已實現 proxy 部位 | 勝／平／負 | 平均淨報酬 % | 中位淨報酬 % |
|---|---:|---:|---:|---:|
| D+5 | 6502 | 2453/0/4049 | -0.348094 | -0.998258 |
| D+10 | 4168 | 1658/0/2510 | -0.414502 | -1.099452 |
| D+20 | 2484 | 898/0/1586 | -1.614442 | -2.390643 |

計算分母僅已實現 raw-price proxy 部位；未入場、未成熟及缺失出場價格分開列於 blocked，零 strict 部位不代表零報酬。

source_manifest 綁定各 Git blob、契約、收據與其餘八份最終序列化檔案的 SHA-256；本報告不是 producer 自我驗證證書。
