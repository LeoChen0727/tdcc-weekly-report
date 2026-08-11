# `revenue_unreacted_range` 低／中位下降候選 forward holdout 規格

## 狀態與用途

本資料層是 `revenue_unreacted_range` 的獨立、事前登記、append-only forward
holdout。它只累積研究證據，不是正式模型，不得提供 daily ranking、scoring、
operation adapter、packet 或 PDF 使用。

所有輸出固定為：

- `research_only=True`
- `formal_model_use_allowed=False`
- `approved_for_daily=False`
- `presentation_allowed=False`
- `promotion_evidence_allowed=False`
- `production_change=False`

規則凍結 anchor 是 PR #462 的 merge commit
`436c25cd0d037c3425ab2ac4fa76cb464cf96de4`。原研究 cutoff 固定為
`20260713`，既有 955 筆 baseline 不重算、不覆寫。PR #462 source projection 另須
精確釘住 `projected_episode_row_count=19569` 與
`projected_episode_semantic_sha256=92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5`；
任一值漂移即 fail closed，不得以 mutable latest 取代。

## 時間分區

| 區間 | 日期 | 用途 |
|---|---|---|
| training | 截至 `20260713` | 只綁定凍結規則與 source projection |
| bridge | `20260714`–`20260803` | 只計數為排除證據，不進 primary holdout |
| primary holdout | 最早 `20260804` | 只使用事件當時已可得資料 |

current wrapper 必須先由價格 frame 的最大交易日取得 observation cutoff，再把同一
cutoff 傳給月營收 source builder。禁止把價格觀察終點之後才出現的月營收更新帶入
本次 capture。

凍結 source projection 的 `episode_end_date` 是 retrospective training boundary，
不是 forward 觀察上限。每一筆 point-in-time qualifying source availability 依原規則
開啟 60 個交易日 watch horizon；as-of 選擇只准取 trigger 當時已可得的最後一筆來源。

## 候選與操作契約

Primary：

- `candidate_variant_id=source_mid_falling`

Challengers：

- `source_low_falling`
- `source_low_or_mid_falling_union`

三者使用完全相同的操作口徑：

- `confirmation_variant_id=delayed_next_close_continuation_bonus`
- trigger 收盤後，D+1 收盤必須高於 trigger 收盤
- D+2 `analysis_open` 進場
- D+30 `analysis_close` 出場
- `holding_session_index_offset=29`，亦即 entry session 為第 1 個持有 session
- `stop_policy_id=none_no_stop_reference`
- 同股前一筆實際出場後的下一個交易日才可重新武裝
- same-stock overlap 必須為 0

若尚未觀察到 D+2 或 D+30，事件保留為 `right_censored`；不得寫入勝率、平均、
中位數或 promotion conclusion。artifact 狀態維持 `holdout_accumulating`，即使已有
成熟列也不得由本資料層自行宣稱通過或失敗。

## PIT 與異常契約

每個 capture 綁定：

- PR #462 merge commit 與 rule canonical SHA-256
- training projection semantic SHA-256 與 manifest canonical SHA-256
- current source detail canonical SHA-256
- 三個 monthly-revenue lineage SHA-256
- price input manifest SHA-256 與逐股票 SHA-256
- observation cutoff、bridge/holdout 日期與 capture id

source availability date、canonical source table date、第一個可交易日不得晚於事件
trigger，source sequence index 亦不得大於 trigger index。異常旗標必須取自實際被選中的
as-of qualifying row；episode aggregate 只可用來核對逐列旗標的一致性，不得讓未來更新
污染較早 trigger。未來 qualifying update 必須列在
`future_qualifying_update_ignored_count`，不得回寫 as-of 特徵或異常旗標。

`unresolved_anomaly_candidate` 保留在 primary metrics；排除候選的結果只能寫入
`excluding_unresolved_anomaly_candidates_sensitivity`。數字門檻只建立
`operation_return_review_candidate_flag`，不是最終異常 disposition。

月營收與季／年財報完全分離。EPS、毛利率、營益率、營業利益、業外與淨利不在
本 holdout 的 gate、score、ranking、PDF 或 promotion evidence 範圍。

## Artifacts

Artifact id：`revenue_unreacted_range_forward_holdout`

每個 capture 產出五個 surfaces：

1. `manifest`：規則、資料 lineage、日期、capture counts 與禁止使用 flags。
2. `event_detail`：每個 disjoint low/mid event 一列；union 由 membership 衍生，不複製事件。
3. `maturity_status`：primary/challengers 的成熟、right-censored、勝和敗與 tail metrics。
4. `comparison`：三個 variant 同一操作口徑的比較；結論固定為 accumulating。
5. `anomaly_sensitivity`：保留候選的 primary 與排除候選 sensitivity 並列。

Latest：

- `output/latest/research_backtest/revenue_unreacted_range_forward_holdout_manifest_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_forward_holdout_comparison_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv`

Append-only history 位於 `output/history/research/`；文件 mirrors 位於
`docs/latest/`。history 以 `(capture_id, artifact_row_key)` 唯一識別；相同 key 的
semantic bytes 不得改寫。完全相同 capture 可 idempotent 重跑。

五個 latest、五個 history 與五個 docs mirror 共 15 個檔案使用同一次 filesystem
publish transaction：所有新 bytes 與 rollback backups 必須先完成 staging，任一 replace
或驗證 I/O 失敗時，15 個 target 全數回復到執行前 exact bytes（原本不存在者仍不存在）。
不得留下部分更新的 latest/history/docs 組合。讀取既有 history、合併與 transaction publish
全程由 exclusive publish lock 保護；並行 writer 必須 fail closed，不得 lost update。

History validator 對五份 history 執行 schema、空白 key、重複
`(capture_id, artifact_row_key)` 與 current capture exact row presence/semantic parity 檢查。
這只是 append-only history structural integrity；舊 capture 的原始 source/price bundles
未隨 history 保存，因此 history hash 或 structural pass **不是**舊 capture 的獨立重播，
也不是 promotion-grade replay bundle 或 promotion proof。

## Producer 與獨立 validator

唯一 model-owned wrapper：

```text
python scripts/build_revenue_unreacted_range_research.py --stage forward_holdout
```

Forward-holdout implementation module：

```text
scripts/revenue_unreacted_range_forward_holdout.py
```

獨立 validator：

```text
python scripts/validate_revenue_unreacted_range_forward_holdout.py \
  --source-detail <exact-source-detail.csv> \
  --price-input-directory <exact-normalized-price-input-directory>
```

validator 不 import forward-holdout producer business functions。它獨立重播 point-in-time
source alignment、120 日位階、下降型態、trigger、D+1 confirmation、D+2 entry、D+30
exit、right censor、rearm/non-overlap、summary/comparison/anomaly metrics，並由 explicit
inputs 重算完整 capture envelope/capture id，再核對五個 current surfaces 與 lineage hashes。
正式 `forward_holdout` stage 在同一批 explicit source、price 與 source manifest 完成
build/write 後，重新讀取 persisted latest surfaces 及五份 history，再呼叫
`validate_frames`。任何 error 使 stage fail closed。Standalone CLI 的五個 history args
預設為已登錄的 `output/history/research/` paths；它不自行重建 business inputs，缺少上述
explicit replay evidence 時會拒絕執行。

研究 workflow input 必須預設 `false`，只能執行本 stage。執行前後必須驗成熟模型
sentinel hashes 不變；任何其他研究 artifact、正式 adapter、readiness、production
snapshot 或 PDF 漂移均 fail closed。
