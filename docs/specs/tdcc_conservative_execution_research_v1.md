# TDCC 潛伏吸籌：保守成交假設研究 v1

owner=`research_backtest`；唯一寫入家族 `tdcc_stealth_accumulation_conservative_execution_research`。
這是 `frozen-ledger replay`，不是正式升級，也不回寫舊 primary。

## 固定政策與範圍

機器政策：`config/tdcc_stealth_accumulation_conservative_execution_research_v1.json`。
於 `2026-09-30T15:29:39+00:00` 固定，早於本次 replay；不是假稱五月已有政策。
只讀既有 ledger `0636fc459583c5e8620fa0c42c948a3d4aaa215e15a6ae27019476d1b9875cc0`，
篩選 `common_12 / validation / D20 / slippage_bps=10` 的 baseline_4（4981）及 trend_8（2986）。
1,000 股、雙邊費率 0.001425／最低20、賣出稅0.003不變。原 entry/exit 日期與價格不變。
不重跑 selector、舊 producer、不補回舊 nonoverlap 已略過訊號；不能推論完整訊號策略的反事實績效。

## 成交假設與鎖

一般列只標 `assumed_regular_price_proxy`，假設款券已備妥、沒有市場衝擊，以原日價代理；
`actual_fill_verified=false`、`execution_evidence_state=unknown` 對所有列都成立。
全市場例外 coverage 未核實，不把欠缺全量清單變成新增普遍門檻，也不稱 verified_normal。
已證處置／特殊制度按事件日期標 unknown，不從成交量、TickType、同價OHLC推論漲跌停或分配。
2492 的 20260504 entry 可用一般假設；20260601 exit 受已證處置影響而 unknown，不回溯取消 entry。
6806 的 20260518 若無更早鎖則 entry unknown；實際 trend_8 先有20260410訊號的未知部位，
因此20260515訊號／20260518入場列是 lock-blocked。按真實事件序列分類，不硬編兩個案例結果。

逐日期處理；同日先 entry-open 後 exit-close。鎖鍵為 model/strategy/固定 `common12-validation`/stock，
兩策略獨立，不能每個 signal_date 換 cohort 避鎖。unknown／partial entry、未完成exit永不自動釋放。
只有涵蓋原完整委託有效期的停止撮合證據能支持 no_entry，單一撮合零分配仍 unknown。
partial 必須是整數 `0 < quantity < 1000`，不算完整成交、零成交或已實現損益。
已知制度只有起日沒有核實結束日，之後維持研究 unknown；不是宣稱歷史限制持續至今。

## 主表與統計

每列原欄位原值及 primary 報酬保留，另列 execution proxy；unknown／partial／blocked／no_entry 報酬空白而非零。
未成交不是虧損。分開列原 primary 代理、全母體未知／不可計算比例、已假設完成子集績效與分母。
原候選235／144保留；候選排除只展示明標敏感度，不用作修正主績效或新選股門檻。
已看過 validation 不能叫未見 OOS；current-version 不是首次發布 PIT。
月營收、EPS、毛利率、營益率、營業利益、業外損益、淨利及季年財報欄位均不納入。

## 交付及保存

本研究的手動入口（本次已產出，不因文件更新重跑）：

```text
python -B scripts/build_tdcc_stealth_accumulation_conservative_execution_research.py --source-ledger <唯讀既有F來源>
python -B scripts/validate_tdcc_stealth_accumulation_conservative_execution_research.py --source-ledger <同一來源>
```

新增 model-owned producer、獨立 validator、兩個 targeted test 檔；不共享模型業務函式。
精確輸出只有本家族的 positions_v1.csv.gz、summary_v1.csv、report_v1.md、source_manifest_v1.json。
付費 FinMind 原始CSV不推repo；政策只留必要衍生查核、hash及來源引用。
正常必要登錄及現有 CI 選路同步；四個 model_data_independence_audit_latest.csv/.md（output/latest及docs/latest）
只同步登錄新增列，沿用原生成時間，不改其他模型語義。不改 workflow、正式模型、adapter/readiness或PDF。

worktree=`F:/CodexStorage/task-worktrees/taiwan-stock-recommendation/tdcc-conservative-execution-research`，
disposition=`retain_until_PR_closeout`；測試暫存只用本 worktree 的 `.pytest-tmp-conservative-v1`，完成後移除。
初始 AvailableFreeSpace：C=50759938048 bytes，F=207519936512 bytes（同 System.IO.DriveInfo API）；
不把磁碟差異一律歸因本工作。終點為可查核研究產物與 PR/checks，合併須另外指示。
