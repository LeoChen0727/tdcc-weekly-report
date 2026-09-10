# TDCC 潛伏吸籌：具歷史版本收據的全市場研究回測 v1

## 用途及禁止用途

本版為 `tdcc_stealth_accumulation` 專屬研究，不是正式模型升級。模型條件、phase/status 為空的既有研究 v2 enum fallback、操作規則、費稅、滑價及持倉鎖均不調整。它不宣稱等同 production phase classifier，也不能支持正式 adapter、PDF 勝率、評分、排序或 promotion。

輸入以歷史當日原始行情的四碼且首碼非零證券為母體，不使用今日存活清單或已篩選的 `all_candidates`。保留 `91` 開頭可能 TDR；四碼規則不等於已逐檔核實普通股分類。

## 固定契約

- selector：`2244a0a36c4542cd62948b50f12ef98ade50e1df` 的研究 v2 enum fallback。
- operation reference：`b4c289c98f7276f07036c1b8b4d90d9d8de466bd`；classifier：`af71f09d64aabbbadf9481940590dce21cd8e263`。
- 當日 decision 僅用 `tdcc_stealth_accumulation_receipted_marketwide_availability_v1.json` 指定、在下一交易日 08:30 Asia/Taipei 前已存在的完整 Git tree。
- 原 39 日收據保留，新增 `20260730`；其餘日期保留缺口，禁止以最新版本補 decision。
- 訊號檢查範圍 `20260615–20260909`；事後 entry/exit 價格固定 `40cee0405390a9ccaf3a1ad0778aa1e680ab8252`，截至 `20260909`。這是明示的新 outcome 版本，不是把後補版本當時點輸入。
- 暖身下限維持 `20260401`；每股至少 21 筆觀察。TDCC 使用同 tree 中有效日不晚於當日的最後四批，缺批／缺值不補零。
- 價格 lag 以同股觀察序列計算，揭露缺交易日；不前填，不新增「21 個市場日必須連續」模型條件。成交量均值與 lineage 檢查只用最後 20 筆，不包含額外第 21 筆。
- 既有 `TPEX_OLD_DAILY_JSON` 成交量 unresolved 規則保留；空白 source 必須揭露其未完整證實，不能宣稱通過來源單位驗證，也不自行新增模型條件。
- 特徵在 selector 判斷前依原規則序列化到小數四位。phase classifier 不執行，`volume_confirmed_breakout=False` 不衍生新條件。

## 買賣及分母

訊號收盤後，下個交易日開盤進場；D+5／D+10／D+20 收盤出場。各窗口獨立維護同股持倉鎖；新訊號日必須嚴格晚於舊持倉出場日。不使用盤中高低作成交價、不加停損停利、不排隊或跨股資金分配。

每筆 1,000 股，雙邊手續費 `0.001425`、每邊最低 20 元，賣出稅 `0.003`，雙邊滑價分別測試 0／10／20 bps。以買進現金為報酬分母。未成熟、缺進場價、缺出場價、持倉鎖阻擋與真正虧損必須分開；不得把缺價或未成熟算為零報酬或失敗。

主要結果含所有未解異常候選；另列排除候選的敏感度，不得稱作修正績效。輸出勝／平／失敗率、平均／中位數、>=10% 率、<=-10% 率及樣本分母。數值幅度、IQR 或少數交易影響只能觸發候選，不能判定資料錯誤並移除。

公司行動及完整歷史交易日曆證據仍未全部核實。strict ledger 不得假設已核實；可計算的數字僅是 `raw_price_cashflow_unadjusted` 研究 proxy，不是總報酬或實際成交。緯穎 `6669` 已知配股事實僅揭露，不套用未證實可交易日期或現金流。

月營收不使用；EPS、毛利率、營益率、營業利益、業外損益、淨利及季度／年度財報全部不在範圍。

## 專屬輸入與輸出

入口：`scripts/build_tdcc_stealth_accumulation_receipted_marketwide_replay.py`。
獨立驗證：`scripts/validate_tdcc_stealth_accumulation_receipted_marketwide_replay.py`，不得 import producer 或執行 production business functions。

輸出目錄為 `output/research/tdcc_stealth_accumulation/`。固定前綴 `tdcc_stealth_accumulation_receipted_marketwide_replay_`，確切九檔為：

- `source_manifest_v1.json`
- `coverage_v1.csv`
- `features_v1.csv`
- `signals_v1.csv`
- `trades_v1.csv`
- `summary_v1.csv`
- `blocked_v1.csv`
- `anomalies_v1.csv`
- `report_v1.md`

manifest 綁定實際讀取的 Git blob／SHA-256 及其餘八檔最終序列化 bytes 的 SHA-256，不自我雜湊。不得寫其他模型或舊版本產物。既有封存目錄不可作新輸出位置。

獨立驗證固定本版 canonical contract SHA `6a6b3a94eae79d6686a9c385d7c4f4bd5b3286dd650ac46d76d0f3ea97e55621` 及 availability SHA `8b09a4ccc4887e4081347b5fecda2ddd8442a659cd0b259dbb9876dce89cef40`。不得只重算 manifest 就替換收據、日曆或刪除原保留異常名單。舊全市場研究清冊的 200 個候選鍵全部承接；已不對應新版交易者仍保留並標記未呈現在當前交易，不能因樣本擴大、IQR 變動或較早持倉替代就宣稱已解決。TDCC 有效比例須滿足 `0 <= p1000 <= p400 <= 100`；違反時整包驗證失敗並要求調查，不直接認定資料錯誤、不剔除列或改變 selector。

## 本地驗證與完成邊界

synthetic tests 必須覆蓋缺收據、日期邊界、每股暖身、last20 成交量邊界、同股持倉鎖、費稅、未成熟、缺價、異常保留、輸出／來源竄改及寫入白名單。獨立 validator 從來源核對數字，不只核對 producer 自證。

本次授權的本地實作、執行及檢查完成後報 `local_validated`；未經 PR／main 驗證不得宣稱正式完成或正式可採用。六份 PDF、Apps Script、workflow、正式條件、舊研究證據均不變。
