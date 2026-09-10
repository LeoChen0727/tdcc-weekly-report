# TDCC 潛伏吸籌公司行動研究帳本 v1

## 目的與邊界

本帳本屬於 `tdcc_stealth_accumulation`（TDCC 潛伏吸籌）專屬的研究證據。
授權依據為 `user_approval_20260910_tdcc_corporate_action_ledger_scope`。
它只將已知公司行動與固定的 v1 研究部位對帳，不重新選股、不改原定買賣、
持有期間、費稅或滑價，也不將事後取得公告當成訊號當時可取得的資料。

固定來源為 `3fe40157cf4b333ef03a1447e45c310d197cbc5b` 的 receipted
marketwide replay v1，來源路徑、位元組數與 SHA-256 列於本 family 的 JSON
契約。涵蓋強生 4747、青雲 5386、益得 6461、緯穎 6669 四檔的全部 90 列
raw-price proxy 交易、59 列訊號與 381 列 blocked 來源。90 列包括
0／10／20 bps 三種滑價情境；10 bps 是 30 個各自帶 D+5／D+10／D+20
持有期間的部位情境，並非 90 筆獨立交易，不同 horizon 亦非獨立樣本。
不得只選價格跳動或獲利較高的列。

## 不可解除的限制

- `coverage_complete=False`：只對帳已封存的五個已知事件，不是全市場、
  四檔全歷史或完整公司行動資料庫。沒有匹配事件不代表證明沒有事件。
- `total_return_verified=False`、`formal_use=False`、
  `promotion_evidence_allowed=False` 固定不變；已核實總報酬欄保持空白，
  不以零報酬代替未知，不產生正式勝率或正式晉升結論。
- 保留來源 strict status 與持倉鎖；`strict_lock_released=False`。
  舊 proxy 出場與這次帳務對帳皆不解除原 strict 未結清部位。
- 異常候選保留在原主要統計與新對帳資料，不改成最終排除理由，不更新舊證據。
- 未知實際交付、帳戶入帳、畸零股處分與其費用不自行補規則；
  不自動延後出場、不使用未來價格出售權利、不假定合併畸零股或無費用到帳。
- 不修改正式模型條件、評分、排序、adapter、readiness、workflow producer
  排程、Apps Script 或六份正式 PDF。
- 月營收、EPS、毛利率、營益率、營業利益、業外損益、淨利、季度／年度財報
  全部不在此研究帳本範圍。

## 日期與權利認列

權利取得日、事件生效日、可交易日、預定付款日與實際付款日必須分開。
日期使用有效的 `YYYYMMDD`；可未知的日期使用空白，非空但非法的日期拒絕。
事件身分、欄位、順序、來源、股份率與現金率均須通過 fail-closed 驗證。

只在 `entry_date < entitlement_date <= exit_date` 時對原部位取得權利。
除權息日才進場不回溯取得舊股權；出場日之後的事件不改原出場日或報酬。
同一權利日的股票股利與現金股利，均使用該日事件發生前的同一股數基礎，
不得先加股票股利後再把新增股份也計算現金股利。

換股事件將原股轉為 `原股數 × share_factor`。如果已知可交易日不晚於
原定出場日，記為已知事件後的理論股數；若晚於出場或未知，記為待交付權利，
不得把已註銷舊股或尚未可交易的新股列作原日可出售股份。
股票股利使用 `原股數 × new_shares_per_old_share`，依同一可交易日判斷
加入理論股數或待交付權利。理論股數不代表個別帳戶已核實交付。

使用 `Decimal` 保留官方精確比率與股數；整股組件與未處理畸零股組件分列。
整股分解只是揭露，不是准許捨去畸零股、替其假定賣價或算已核實總報酬。
若尚有未交付權利又跨越後續權利日，因缺少權利再參與分配的核准契約而拒絕。
即使新股份在最終出場日前已可交易，也不得將股數追溯加到更早的另一權利日。
可交易日與後續權利日相同時，因同日先後未經證實亦拒絕；只有更早可交易的
股份，才在後續不同權利日的理論股數基礎內。

現金股利按該權利日原股數算公告毛額應收；預定付款日已過不等於已收到。
只有明確 `payment_confirmed=True`、有效且不晚於原出場的
`actual_payment_date`、非空 `payment_confirmation_ref` 同時存在，才可
在合成測試中認列已收款項。本次真實來源未提供任何個別現金入帳確認，
故不得由公告日期或預定日期推論已收。未知金額保持空白，公告明示的零才是零。

## 五個固定事件

| 股票／事件 | 權利取得日 | 生效／可交易日 | 帳務解釋 |
| --- | --- | --- | --- |
| 強生 4747 換股 | 20260820 | 20260831／20260831 | 每舊股換 2 股；20260820～20260828 停止買賣 |
| 青雲 5386 股票股利 | 20260720 | 20260720／20260814 | 每舊股新增 0.50000001386 股；8/14 為新股權利證書可交易日 |
| 青雲 5386 現金股利 | 20260720 | 20260720／不適用 | 每舊股公告 1.5 元；8/14 只為預定付款日 |
| 益得 6461 減資換股 | 20260902 | 20260909／20260909 | 每舊股換 0.618578 股；虧損彌補減資，退還股款明示 0；不等於畸零股處理已完成 |
| 緯穎 6669 股票股利 | 20260902 | 20260902／未知 | 每舊股新增 1.98279460 股；取代較早版本比率，認購繳款區間不是交付日 |

青雲原研究 7/22 與 8/5 出場皆早於 8/14，新增權利必須未結清，不可乘上
未來可交易股數後冒稱原日全部售出。緯穎沒有確定可交易日，新增權利亦不可當日
出售。強生及益得即使可辨識理論換股，仍未解決所有完整 coverage、個別入帳與
畸零股契約，因此仍不核發總報酬或正式勝率。

## 來源與產物契約

`config/tdcc_stealth_accumulation_corporate_action_ledger_v1.json` 包含封存
官方原始回應與其 SHA-256、bytes、URL、取得日期、可用的 request receipt。
先驗證原件 bytes 與固定來源 SHA，再驗證事件欄位與公告證據的關係。
事後來源保留 `first_publication_verified=False` 與
`original_revision_chain_verified=False`；不得改成完整 PIT 版本鏈。
來源訊號、交易、blocked 的 canonical 全欄 row hash 保留，不只 hash 用到的
幾個欄位；原 proxy 報酬只原樣揭露，不重新計算或覆寫。

model-owned producer 為
`scripts/build_tdcc_stealth_accumulation_corporate_action_ledger.py`，
唯一五個寫入產物位於 `output/research/tdcc_stealth_accumulation/`，共同前綴為
`tdcc_stealth_accumulation_corporate_action_ledger_`：

- `source_manifest_v1.json`：固定來源、官方原件、配置及最終序列化產物雜湊。
- `events_v1.csv`：五個事件的明確時間與股數／現金率。
- `positions_v1.csv`：四股全部 90 列原 proxy 部位與未結清對帳狀態。
- `blocked_v1.csv`：保留原 strict 阻擋來源及本次對帳阻擋，不釋放部位。
- `report_v1.md`：樣本口徑、已知事件差異與未解限制；不是績效修正報告。

writer 必須拒絕第六個檔名、遺漏檔、任意相對路徑、跳脫路徑、symlink／reparse
來源或目的地；只可寫 exact 五個已登錄名稱。CSV／JSON 使用穩定序列化，manifest
綁定最終 bytes，不以可變 `latest` 取代版本化證據。

## 驗證與執行

獨立 validator
`scripts/validate_tdcc_stealth_accumulation_corporate_action_ledger.py`
不得 import producer 或正式模型的商業函式；自行讀取固定來源、檢查 hashes、
身分、原列保留、事件時序、股份／現金組件與全部 fail-closed 欄位。
測試檔為 `tests/test_tdcc_stealth_accumulation_corporate_action_ledger.py`。

synthetic regression 覆蓋 ex 日進場、可交易日前／同日／後日出場、同日股息共用
舊股基礎、精確換股／減資、未知交付及現金、未來事件、重複或不明來源、非法日期、
負值與非有限數值、來源及產物竄改、strict lock、五檔 writer 與 validator 獨立性。
合成結果不得當成真實交易績效。

CI 僅新增本帳本的 validator、synthetic regression 與產物無漂移檢查，不新增
producer workflow 或排程。完整交付仍需正常 PR checks、main 合併與合併後官方
`validation_profile=all` 證據；分支或本地通過不代表正式模型已可採用。
