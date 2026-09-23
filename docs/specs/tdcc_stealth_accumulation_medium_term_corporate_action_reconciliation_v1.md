# TDCC 潛伏吸籌：固定中期交易公司行動對帳 v1

這是模型專屬的新研究證據，不是完整公司行動資料庫、重新選股或正式勝率。
授權為 2026-09-23 使用者「授權所有要求」的兩模型獨立公司行動研究修復。

## 固定來源與保留

Git `001b82f856c4ca1a863d64998890fb1fdfba8030` 的
`tdcc_stealth_accumulation_medium_term_trend_research_trades_v1.csv.gz`
305,673 列完整保留。綁定來源 bytes SHA-256、每列全欄 canonical SHA-256，
原條件、策略、profile、partition、股票、日期、股數、費稅、滑價、持有期、
報酬、異常旗標及 strict status 一律不改。沒有重跑 selector，沒有移動進出場。
舊十一份中期研究產物、舊公司行動帳本及其他既有證據全部保持不變。

## 三個事後收件官方事件

| 股票 | 每舊股換新股 | 停止買賣 | 官方換股基準日 | 新股開始交易 |
| --- | --- | --- | --- | --- |
| 可寧衛 8422 | 10 | 20251106–20251114 | 20251114 | 20251117 |
| 寶雅 5904 | 10 | 20260730–20260807 | 20260807 | 20260810 |
| 虹光 2380 | 0.27658171 | 20260617–20260626 | 20260626 | 20260629 |

三份官方原件以 UTF-8 response bytes/base64、URL、實際收件時間與 SHA-256
封存在本 family JSON 契約。2380 精確比率來自 TWSE 公告每壹仟股換
276.58171 股，不從參考價格反推，也不借其他模型的價格調整 registry。
公告日期及今日原文不能證明首次發布版本或原始更正鏈。

`holding_cutoff_date` 是停止交易首日，只用來辨識舊持股跨換股的 frozen
position，不冒稱官方權利取得日；官方 `record_date`、`suspension_end`、
`effective_date`、`tradable_date` 各自分列。原進場若落在停牌期間直接阻擋。
`entry < holding_cutoff <= exit` 才計理論換股。退出若早於新股可交易日或日期
未知，列為 pending rights，不把已終止舊股或未交付新股售出，不延後退出。

## 可比較價格與不可宣稱的報酬

`theoretical_exit_shares` 使用 Decimal 精確乘官方比例。整股、分數股與
未結清權利分列；不能捨去分數股、假定補足、處分費用、售價或現金入帳。

`known_action_gross_price_proxy_pct` 僅是已知換股後理論股數乘原退出收盤價，
相對原始進場價值的股價可比算術。可以揭露分數股算術，但不是分數股已成交，
不是淨報酬、總報酬或正式操作績效。未知公司行動現金及股利不在其內。

`known_action_costed_proxy_pct` 僅限整股、已知原日可交易且換股現金明示為零的
合成／已核實事件條件，沿用原費稅滑價，仍不得稱真實總報酬。本次三份原文沒有
明示現金退還額，`cash_per_old_share` 留空，實際三事件不產生成本後 proxy。
股利與完整其他事件未證明；未知不是零，公告付款日不是實收。

未匹配事件的 proxy 留空，「沒有登錄事件」不等於「證明沒有事件」。
每列 `coverage_complete=False`、`total_return_verified=False`、
`verified_total_return_pct` 空白、`formal_use=False`、
`promotion_evidence_allowed=False`。所有舊異常候選保留，不自行最終分類或排除。

summary 保留原 primary 的原樣平均，另列已匹配事件、理論價格可比、條件成本
proxy、分數股、未交付權利各自樣本數與分母。不得合併為全市場修正勝率；
條件子集不代表全部市場，更不是策略門檻調整依據。

## 檔案、獨立驗證與執行

唯一 writer 為
`scripts/build_tdcc_stealth_accumulation_medium_term_corporate_action_reconciliation.py`。
唯一六份新產物位於 `output/research/tdcc_stealth_accumulation/`，前綴為
`tdcc_stealth_accumulation_medium_term_corporate_action_reconciliation_`：

- `source_manifest_v1.json`
- `events_v1.csv`
- `positions_v1.csv.gz`
- `blocked_v1.csv.gz`
- `summary_v1.csv`
- `report_v1.md`

CSV 採 UTF-8/LF；gzip mtime=0；manifest 綁定實際輸出 bytes。
契約 canonical SHA-256 為 JSON sorted keys、ensure_ascii=False、
separators=(',', ':') 的 UTF-8 bytes。producer 與獨立 validator 各釘選契約 hash。

獨立 validator 不 import producer 或其他模型商業函式；自行核實官方原件、
精確比率與日期、frozen rows 全欄保留、算術、未知狀態、完整分母及產物 hash。
synthetic tests 涵蓋換股、分數股、未知現金、退出／可交易日邊界、重複事件、
來源／產物變造與精確六檔 writer。CI 的 published test 不得因缺產物而 skip。

CLI 為各 script 加 `--repository-root <approved-F-task-worktree>`。
producer 只讀釘選 Git blobs，不 materialize 舊 output/data，不需私人來源。
登錄完成後才執行；產物精確 allowlist 與前後 Git tree/index／實體 bytes
snapshot 阻擋所有範圍外寫入，未知檔案全部保留。

月營收、EPS、毛利率、營益率、營業利益、業外損益、淨利及季／年財報全部
排除。不修改正式模型、評分、排序、買賣規則、adapter/readiness、workflow、
Apps Script 或六份 PDF。正式總報酬、首次發布 PIT、真正未見樣本外與完整覆蓋
仍未成立；本 PR 技術驗證不解除上述研究限制。
