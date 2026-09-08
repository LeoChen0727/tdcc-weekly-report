# TDCC潛伏吸籌模型 historical selector field-contract repair replay v2

## 結論

本報告以固定 `7ef37a966280201a5ee236856306fdb513de7092` 的選股條件為基礎，套用本次 research-only 欄位修復版本；不是 production selector，也不是當時實際發布推薦。資料日期為 20260615–20260907，共讀取 36 個 immutable commit-bound 候選快照、19361 列候選，v2 選出 6821 signal rows、520 stocks；其中與實際發布的 `tdcc_stealth_accumulation` 推薦相符 0 列。同母體 v1 current-rule replay 仍為 0 列。

## 研究績效（未扣交易成本）

| 持有窗 | 可評估 | 右設限 | 勝 / 平 / 敗 | 勝率 | 平均報酬 | 中位報酬 | 高報酬命中 | 列級自動候選數（任一窗觸發） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D5 | 5706 | 1115 | 2037 / 84 / 3585 | 35.699264% | -2.288835% | -2.090592% | 309 | 1 |
| D10 | 5082 | 1739 | 1498 / 60 / 3524 | 29.476584% | -5.351211% | -4.717073% | 327 | 1 |
| D20 | 4322 | 2499 | 1072 / 34 / 3216 | 24.803332% | -8.255696% | -7.969639% | 337 | 1 |

## 既有條件逐步診斷

以下依 `cond_tdcc_stealth()` 的實際短路順序統計；首次拒絕數是上一關剩餘數減本關剩餘數，未新增任何條件。

| 既有判斷步驟 | 通過後剩餘 | 本步首次拒絕 |
|---|---:|---:|
| 排除 `price_leading_tdcc` / `overheated_after_tdcc` phase | 19361 | 0 |
| 排除既有 attack-already-started（含 `volume_confirmed_breakout`） | 15391 | 3970 |
| 量比空白或 `<2.5` | 14900 | 491 |
| `tdcc_leading_price` 或空白 phase + `tdcc_positive` fallback | 8434 | 6466 |
| 5日報酬空白或 `<8%` | 7568 | 866 |
| 20日報酬空白或 `<20%` | 6821 | 747 |
| 收盤位於近20日區間上下 10% 容許帶 | 6821 | 0 |

## 欄位契約診斷

在通過 attack 與量比後的 14900 列中，`tdcc_price_phase` 欄位 missing / blank / nonblank = 14900 / 0 / 0；實際選值分布為 `<blank>` 14900。
`tdcc_status` / `tdcc_judgement` / `tdcc_judge` alias 組合 missing / blank / nonblank = 0 / 14900 / 0；實際選值分布為 `<blank>` 14900。
`tdcc_accumulation_signal` missing / blank / nonblank = 0 / 77 / 14823；原始值分布為 `<blank>` 77、`distribution_warning` 6340、`mild_accumulation` 6013、`neutral` 49、`strong_accumulation` 2421。
其中 `mild_accumulation` + `strong_accumulation` 共 8434 列，但 source commit 的 `tdcc_positive()` 對此欄位套用 boolean `flag()`，只接受 `true/1/yes/y/t`。因此 current-rule replay 必須維持 0 命中；v2 只在 phase 與 status 皆空白、且既有 boolean 路徑未放行時，依獨立研究欄位契約將 `mild_accumulation` / `strong_accumulation` 解讀為正向 fallback；`distribution_warning` / `neutral` 與 unknown 不放行。其他衝突只揭露並保留既有優先序。此修復不改 production selector。

## 口徑與限制

- 入場：訊號日收盤確認後，下一個有該股票有效價格列的交易日開盤。
- 出場：D5、D10、D20 固定未來收盤，只是研究比較窗，不是正式操作契約。
- 成本：報酬為未扣手續費、交易稅與滑價的 gross return。
- 同股後續/重複訊號：`overlap_with_prior_signal=True` 只表示同股票已有更早 signal；不是依 D5/D10/D20 持倉窗驗證的真正重疊部位。全部 signal rows 保留於 primary metrics，因此結果是訊號列加權，不是獨立部位或投組績效。
- 異常：表中各 horizon 顯示的是同一組列級自動候選（任一窗觸發），不是各窗各自新增；本次為 `8261` 20260616（abs_return_d10_ge_80pct）。候選仍保留於 primary；排除後僅為 sensitivity，不能稱為修正績效。
- PIT：候選與價格檔均綁定 source commit 與 SHA-256，但 snapshot `generated_at` 不是完整 event-time filed-at 證明；價格調整／公司行動基礎尚未權威核實。`invalid_price_count=0` 只表示既有價格有效性檢查通過，不證明交易日完整性或調整基礎。
- phase / status / enum：不呼叫共用 phase classifier；保留 current selector 的 phase、status alias 與 boolean 行為，只對兩者空白時的已知正向 enum增加研究 fallback。
- 正式界線：`formal_use=False`、`trade_eligible=False`、`promotion_evidence_allowed=False`。

## 來源綁定

- source ref: `7ef37a966280201a5ee236856306fdb513de7092`
- source commit: `7ef37a966280201a5ee236856306fdb513de7092`
- source commit time: `2026-09-07T18:39:08Z`
- production source SHA-256: `93ad31cedbc7132a4f34a6e83fd34b0ed163bcd1e7f47b722a0727d0a3acdd6c`
- selector contract SHA-256: `13b511f898de561c4c42d8c17dd857b9e55b87b829d8421b95eca951b5ba4767`
- detail SHA-256: `4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3`

## v1 / v2 比較界線

- v1 current-rule replay：同一歷史母體選出 0 列，原因是 enum 被 boolean `flag()` 讀取。
- v2 field-contract replay：同一歷史母體選出 6821 列；這不是 `8434`，後者只是通過前三關且 enum 為正向的診斷列數。
- 三個上游 enum producer 的 strong/mild 細節不同，snapshot 無法證明逐列 producer branch；只採共同允許值語意。
- 結論仍為 advisory-only；不得作 promotion、正式 ranking/scoring、PDF 或 operation evidence。

## 大幅報酬有界 spot-check 待解清單

下列僅列各 horizon 的 observed min/max，最多六組。`automatic anomaly candidate` 仍只有既有 `abs(return)>=80%` 規則標記的列；本表其他數字是人工查核待解觀察，不是新增排除規則。來源價格序列連續只代表 immutable source 中從 entry 到 exit 可取得預期列數，不能替代公司行動、除權息或調整基礎的權威證據。

| horizon | observation | stock | signal | entry | exit | return | source sequence | entry SHA-256 | exit SHA-256 | status |
|---|---|---|---|---|---|---:|---|---|---|---|
| D5 | observed min | 2492 華新科 | 20260709 | 20260713 @ 473.500000 | 20260720 @ 277.000000 | -41.499472% | available_source_sequence_matches_D_horizon | `d6ffdaa42cccb33cdd74a55ee2d1cf468d37268d2459ebcbd43ce7840a47cbc7` | `57229ad0aca43d78cbd9c6b333ebbb84b4ddf52ab16cb54e0bcc311d472cf898` | unresolved; retained in primary |
| D5 | observed max | 1447 力鵬 | 20260626 | 20260629 @ 6.400000 | 20260706 @ 9.510000 | 48.593750% | available_source_sequence_matches_D_horizon | `b1291bf7f405b215e0a800e2ef35a363e1848ec9db716977020cd1edbfe91b83` | `c7e3aeba582481aa00f8a18553ca5651b853a8fd8fb2e52397d1d40c3e37adcd` | unresolved; retained in primary |
| D10 | observed min | 3624 光頡 | 20260714 | 20260715 @ 120.000000 | 20260729 @ 62.300000 | -48.083333% | available_source_sequence_matches_D_horizon | `52e4773de2880da63becd84c41439e4d577d0fd1900c8a56e176086a109448e9` | `c73c5a0617fe7cab53c97ce9a53cef1e1f1252d612748f70b438cf678c987d84` | unresolved; retained in primary |
| D10 | observed max | 8261 富鼎 | 20260616 | 20260617 @ 176.000000 | 20260702 @ 327.000000 | 85.795455% | available_source_sequence_matches_D_horizon | `6f1d791b49276f0f5455d848e788066591491fd512012e44309be0fbdff133a4` | `43d77ac58ef33b3e8d9ed75395a229cf4a308f1d60d1449198f2a7ac703ab58c` | unresolved; retained in primary |
| D20 | observed min | 8358 金居 | 20260630 | 20260701 @ 626.000000 | 20260730 @ 271.000000 | -56.709265% | available_source_sequence_matches_D_horizon | `1cf8d05ccc3edb9f2a861b2942a3b4159f5e3ecb18aaa80b20e6b6240e894553` | `8362199c0bd89bbcbb1b1557706634d929a0c7a335851074f64df75bc02bf6c9` | unresolved; retained in primary |
| D20 | observed max | 3653 健策 | 20260717 | 20260720 @ 3175.000000 | 20260817 @ 5340.000000 | 68.188976% | available_source_sequence_matches_D_horizon | `57229ad0aca43d78cbd9c6b333ebbb84b4ddf52ab16cb54e0bcc311d472cf898` | `584c81a07e0564d854a559ff7b1ce376a005f1827385d00b31ea52480c0b7ef0` | unresolved; retained in primary |
