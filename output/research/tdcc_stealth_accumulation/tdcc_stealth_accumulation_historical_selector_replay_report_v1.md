# TDCC潛伏吸籌模型 historical selector research replay v1

## 結論

本報告是固定 `7ef37a966280201a5ee236856306fdb513de7092` 現行 selector 套用歷史候選快照的研究重建，不是當時實際發布推薦。共讀取 36 個 immutable commit-bound 候選快照、19361 列候選，重建選出 0 列；其中與實際發布的 `tdcc_stealth_accumulation` 推薦相符 0 列。

## 研究績效（未扣交易成本）

| 持有窗 | 可評估 | 右設限 | 勝 / 平 / 敗 | 勝率 | 平均報酬 | 中位報酬 | 高報酬命中 | 未解異常候選 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D5 | 0 | 0 | 0 / 0 / 0 | —% | —% | —% | 0 | 0 |
| D10 | 0 | 0 | 0 / 0 / 0 | —% | —% | —% | 0 | 0 |
| D20 | 0 | 0 | 0 / 0 / 0 | —% | —% | —% | 0 | 0 |

## 既有條件逐步診斷

以下依 `cond_tdcc_stealth()` 的實際短路順序統計；首次拒絕數是上一關剩餘數減本關剩餘數，未新增任何條件。

| 既有判斷步驟 | 通過後剩餘 | 本步首次拒絕 |
|---|---:|---:|
| 排除 `price_leading_tdcc` / `overheated_after_tdcc` phase | 19361 | 0 |
| 排除既有 attack-already-started（含 `volume_confirmed_breakout`） | 15391 | 3970 |
| 量比空白或 `<2.5` | 14900 | 491 |
| `tdcc_leading_price` 或空白 phase + `tdcc_positive` fallback | 0 | 14900 |
| 5日報酬空白或 `<8%` | 0 | 0 |
| 20日報酬空白或 `<20%` | 0 | 0 |
| 收盤位於近20日區間上下 10% 容許帶 | 0 | 0 |

## 零樣本資料契約診斷

在通過 attack 與量比後的 14900 列中，`tdcc_price_phase` 欄位 missing / blank / nonblank = 14900 / 0 / 0；實際選值分布為 `<blank>` 14900。
`tdcc_status` / `tdcc_judgement` / `tdcc_judge` alias 組合 missing / blank / nonblank = 0 / 14900 / 0；實際選值分布為 `<blank>` 14900。
`tdcc_accumulation_signal` missing / blank / nonblank = 0 / 77 / 14823；原始值分布為 `<blank>` 77、`distribution_warning` 6340、`mild_accumulation` 6013、`neutral` 49、`strong_accumulation` 2421。
其中 `mild_accumulation` + `strong_accumulation` 共 8434 列，但 source commit 的 `tdcc_positive()` 對此欄位套用 boolean `flag()`，只接受 `true/1/yes/y/t`。因此 current-rule replay 必須維持 0 命中；這是歷史 snapshot 與 current selector 的欄位語意不相容，不能解讀為真實沒有正向 TDCC 狀態，也不能在本研究中擅自 reinterpret enum。

## 口徑與限制

- 入場：訊號日收盤確認後，下一個有該股票有效價格列的交易日開盤。
- 出場：D5、D10、D20 固定未來收盤，只是研究比較窗，不是正式操作契約。
- 成本：報酬為未扣手續費、交易稅與滑價的 gross return。
- 同股重疊：全部保留於 primary metrics，並在 detail 標記。
- 異常：數值觸發只標記 `unresolved_anomaly_candidate`，仍保留於 primary；排除後僅為 sensitivity，不能稱為修正績效。
- PIT：候選與價格檔均綁定 source commit 與 SHA-256，但 snapshot `generated_at` 不是完整 event-time filed-at 證明；價格調整／公司行動基礎尚未權威核實。
- phase：不呼叫任何共用 `classify_tdcc_price_phase()`；完整保留現行空白 `tdcc_price_phase` 加 `tdcc_positive` fallback。
- 正式界線：`formal_use=False`、`trade_eligible=False`、`promotion_evidence_allowed=False`。

## 來源綁定

- source ref: `7ef37a966280201a5ee236856306fdb513de7092`
- source commit: `7ef37a966280201a5ee236856306fdb513de7092`
- source commit time: `2026-09-07T18:39:08Z`
- production source SHA-256: `93ad31cedbc7132a4f34a6e83fd34b0ed163bcd1e7f47b722a0727d0a3acdd6c`
- selector contract SHA-256: `80e38fda5b737946589f11f182a15d2bc588be6413819b908aff453e0b146d5b`
- detail SHA-256: `0b7b659698740f54dd05e37989cb60a802f3787fc5f499e3a5d41a9c77502a81`
