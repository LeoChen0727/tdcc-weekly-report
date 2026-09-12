# TDCC 潛伏吸籌一年目前版本研究回放 v1

本版是**使用目前取得歷史版本的 research-only 回放**，不是 strict PIT、已核實 total-return、正式操作勝率或 promotion evidence。使用者於 20260912 授權另版整合、實際一年回放與必要驗證；不是舊三個月 receipted replay 的修訂。

## 單一 owner 與輸入

owner 為 `tdcc_stealth_accumulation_current_version_annual_replay`，僅 `scripts/build_tdcc_stealth_accumulation_current_version_annual_replay.py` 寫入九份新產物。契約為 `config/tdcc_stealth_accumulation_current_version_annual_replay_v1.json`；65份外部檔案以相對路徑、SHA256及用途逐筆列舉。付費 FinMind 55份原始CSV保持私有，不進 Git、PR 或 Pages。

- 51週年度 TDCC 加4週暖機：20250815至20260904，共3,667,325原文列。調整與 total 不當作普通級距。
- 訊號與結果截止：20250910–20260909；暖機日價起點20250401，實際最早既有日價20250407。55週不是55週都可評估；不延伸至不存在的20260911 TDCC。
- 日價直接以 immutable Git-ref 讀取 `data/daily_price/YYYYMMDD.csv`，source SHA `07d992bbd9afa283355d8828a294da4524efb56d`，包括 PR #681 已修復18個10月日期。不讀 `data/stock_price_history`、pre681 cache 或 `daily_price_YYYYMMDD.csv` alias；不用新版本覆寫舊回測 receipt。
- main 缺20250915，由既有 `recovered_price_20250915.csv` 提供本版獨立研究來源。只允許補 absent day；原檔 approval flags 不改。
- 七股八份既有 TPEx 官方月行情 JSON 只補暖機有效觀測，張數乘1000為股數；`--` 不補零。既有有效 main 同日列優先，兩個有效來源若OHLC/volume不一致則停止。五個近期上市／身分轉換代碼不拼接前身。
- 現行官方日曆與固定 main 例外休市記錄形成 proxy session calendar；原始發布版本及完整臨時休市事件未認證。

母體沿每個歷史訊號日實際行情 `[1-9][0-9]{3}`，不是今日存活名單，也不是已認證普通股集合；`91` 開頭另標可能 TDR。缺日、缺TDCC、缺OHLC和未成熟分別揭露，不新增任意剔除門檻。

## 凍結語意

selector commit `2244a0a36c4542cd62948b50f12ef98ade50e1df`；classifier commit `af71f09d64aabbbadf9481940590dce21cd8e263`，其 `tdcc_trend_utils.py` blob id為 `200d331615a9910b9436b2304a234ce1d6d602e4`。不得將 blob id 誤當 commit。只載入明列 pure AST 函式，不呼叫舊 producer、不 monkeypatch ROOT。

同一模型的凍結 selector 純函式為本版明確批准依賴；其餘年度輸入組裝、特徵和現金流程式碼由本版獨立持有，修改本版不改舊版。四批TDCC有效日<=signal；400/1000最後減第一、up為相鄰增加次數。strong 是雙delta>0且各up>=2；否則任一delta>0為mild（另一delta可負）。缺批／缺值 unsupported。

phase/status明確留白、`volume_confirmed_breakout=False`；固定 v2 enum fallback 與內建OHLCV attack exclusion不變。每股最後21個現有觀測、5/20 observation lag、當日含於20均量高低、前20高排除當日、shares/1000 lots；四位數值序列化順序維持。現有觀測中無效OHLC仍使該窗 unsupported；缺市場日只披露、不前填，不加60日或連續市場日 gate。

## 操作與限制

D0 下一交易session open；D+5/10/20為`calendar[entry_index+h]` close，各持有期同股持倉鎖獨立，new signal必須嚴格晚於上次exit。固定1000股、雙邊fee0.001425/min20、sell tax0.003、slippage0/10/20 bps。缺entry、缺exit、未成熟與因持倉阻擋不混為失敗交易。

raw unadjusted cashflow proxy 與 strict ledger分開。無原始可得性證據時strict為`blocked_input_availability_unproven`，不得由proxy出場解除strict鎖。無公司行動現金流／股數完整證據，不宣稱零公司行動、實際成交或核實總報酬。

舊未解候選保留；本版Q1/Q3±3IQR只產生調查候選。所有未解候選保留primary；排除候選只作 sensitivity，不是 corrected/cleaned performance。未追根查因前不作promotion結論。本文不開啟新調參或異常來源研究。

本版不使用月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利及季度／年度財報全部排除。

## 九份產物與驗證

相同前綴 `tdcc_stealth_accumulation_current_version_annual_replay_`、後綴 `_v1`，位於 `output/research/tdcc_stealth_accumulation/`：

| kind | 格式 | 用途 |
|---|---|---|
| source_manifest | JSON | 固定契約、Git/blob/external SHA、calendar、counts、其他8份最終bytes hash |
| coverage | CSV | 每日母體與支持度、缺來源；PIT supported恆0 |
| features | CSV.GZ | 全母體特徵與unsupported原因；不刪掉未支持列 |
| signals | CSV.GZ | supported且通過凍結selector的原樣特徵列 |
| trades | CSV.GZ | 各horizon與成本情境的raw-price現金流proxy |
| summary | CSV | 3持有期×3成本×primary/sensitivity=18列 |
| blocked | CSV.GZ | 特徵unsupported、未入場、未成熟、缺exit及strict ledger |
| anomalies | CSV | 未解候選及當期是否有對應proxy |
| report | Markdown | 使用者可讀結果與不可外推限制 |

gzip deterministic mtime=0。壓縮只控制交付大小，不抽樣、不改列。原始私有CSV不內嵌，也不發布其完整內容。

獨立 validator 不匯入 producer／production business functions。CI `--published-only` 驗最終實體九檔、hash、表間集合、selector/cashflow/summary/strict/anomaly不變量；它不冒稱CI能讀私有55份輸入。F上的完整模式另讀真實來源與immutable Git blobs重算。合併後 main all及本地完整模式都須通過，才能聲稱本次工程完成；研究採用與PIT仍受限制。

正常生產PDF、formal adapter、舊TDCC三個月/PIT證據、TDCC weekly與Apps Script均不在寫入範圍。四份 `model_data_independence_audit_latest` 只同步新家族登錄所需治理快照，不是新回測成果。

### 精確驗證命令

本機完整來源核對（將 `<private-input-root>` 替換為本次已授權私有目錄，不上傳該目錄）：

```text
python scripts/validate_tdcc_stealth_accumulation_current_version_annual_replay.py --input-root <private-input-root> --price-repository-root <fixed-source-repository>
```

公開產物CI與聚焦回歸：

```text
python scripts/validate_tdcc_stealth_accumulation_current_version_annual_replay.py --published-only
python -m pytest -q tests/test_tdcc_stealth_accumulation_current_version_annual_replay.py tests/test_validate_tdcc_stealth_accumulation_current_version_annual_replay.py
```
