# TDCC 潛伏吸籌中期整體趨勢研究 v1：運算前方法預註冊

## 狀態與範圍

本方法於新研究績效運算前登錄；不是新取得的盲測。先前年度回放、期間延伸及條件分層結果已被研究者看過，本次 20260401 後的時序驗證不宣稱 genuine unseen OOS。
唯一模型為 `tdcc_stealth_accumulation`，全案 `advisory-only`；`formal_use=False`、`promotion_evidence_allowed=False`。
新程式不得變更舊年度 producer、舊研究證據、正式 selector/參數/排名/評分、operation adapter/readiness、PDF 或 Apps Script。

## 固定來源

- 實作起點：`847d774ca80f354253e4680e32bc1a46584e35c0`。
- 年度來源契約／不可變基準：`d2f3ccfaf95562b5179f433af0b4b41d62bfee17`。
- 價格：`07d992bbd9afa283355d8828a294da4524efb56d`。
- `as_of=20260909`；signal 範圍 `20250910..20260909`。
- 55 批既有 TDCC，`20250815..20260904`。原年度契約明列的 65 個私有輸入須逐個驗證 SHA-256；不新下載、不公開付費原文。
- 私有輸入根：`F:/CodexStorage/retained-evidence/taiwan-stock-recommendation/finmind-tdcc-intake-20260912`。
- 年度保留證據：`F:/CodexStorage/retained-evidence/taiwan-stock-recommendation/tdcc-current-version-annual-replay/deliverables`。
- 以 TDCC 有效日 `d <= signal_date` 取已取得歷史版本，僅 current-version availability proxy；原始發布可得性未證明，不是 strict PIT。

## 全市場資格母體與比較

逐歷史價格日重建四位且不以 0 開頭的代碼母體，不使用今日存活名單，也不使用舊 210140 selected signals 作為資格母體。
91 開頭可能 TDR 保留並揭露，不宣稱逐股普通股分類已核實。新舊身分不拼接。
獨立保留原價量有效性、暖機、四位小數序列化與原研究 v2 enum fallback 價量條件；不把舊 `feature_supported`（混合價量與四批TDCC缺值）當純價量 gate。
不暗中保留四批 TDCC selector 作新八／十二批條件的前置篩選。

策略固定為：

1. `baseline_4`：完整重建原四批 TDCC 條件，僅作舊法基準。
2. `trend_8`：主研究，當期最後八批 400+ 與 1000+ 持有比例對實際日期的 OLS slope 均嚴格大於 0。
3. `trend_12`：穩健性研究，相同規則改用當期最後十二批。

`full_available` 各策略使用自己的全部可支持歷史。
`common_8` 的四批基準與八批趨勢使用相同價量與八批完整歷史資格母體，從共同起點空倉各自重播。
`common_12` 的四／八／十二批策略使用相同價量與十二批完整歷史資格母體，從共同起點空倉各自重播。
共同母體是資料資格交集，不是策略訊號交集；不只讓四批基準攜帶共同起點前的持倉。
完整／共同母體分開報告，量化批數不足、缺股、缺開市週及其造成的資格／訊號損失；不得將不同期間的差異稱為策略優劣。

## 日期與精確斜率

從原文 `比例` 使用 Decimal 精確加總 400+ 的四個級距；1000+ 為最高級。調整／total 列不納入。
對當期最後 N 個全市場批次日期，以第一批為零點、`d` 為整數日差、`p` 為持有百分比：

`slope_pp_per_week = 7 * (N * sum(d*p) - sum(d)*sum(p)) / (N * sum(d*d) - sum(d)^2)`。

正負判定使用精確分子，不先轉 float、不先四捨五入、不加 epsilon；常數與對稱升降序列的零斜率拒絕。
允許中途下降。端點淨變化、最近一次回落與單次上升占比僅為描述／高低報酬特徵，不是額外 gate。單次上升占比固定為 max(正向相鄰變化)/sum(正向相鄰變化)，無正向變化則缺值並記 reason，不影響策略資格。
每股當期 N 批缺任一必要比例即 unsupported，不以更舊批補足、不補零、不前填。
批次不等於完整日曆週；報告批數及實際日曆跨度。不得使用 `gap == 7` 判定完整性。
週界固定週一至週日，自第一個所選批次起，檢查直到 signal_date 前已完整結束的最後一週，包含最後一批之後的完整週。用 SHA-bound 官方交易日曆區分整週休市與整個開市週缺批；當週尚未結束不當作缺批，日曆證據不足則 unsupported，不宣稱 coverage verified。例：signal=20251020、末批=20251009，20251013..19 開市卻缺批則 unsupported；signal=20251016 時該週未完，不誤判。

## 操作、分界、統計與限制

保留原 next-trading-day-open 進場、收盤出場、D20 主分析／D60 次分析、1000 股、買賣各 0.001425 且各最低 20 元、賣出稅 0.003、slippage 0/10/20 bps。
各策略／共同母體／horizon 獨立同股非重疊鎖；原訊號須嚴格晚於上一筆 exit_date，沿用成熟度規則。不得使用盤中高低價當實現交易價。
依 entry_date 分 train／validation，分界 `20260401`；signal=20260331、entry=20260401 屬 validation。
`purged_cross_split` 列不納入 train/validation 績效，但仍占用原完整時序的鎖；分界不可重置持倉。
在解釋條件前先比較固定買賣規則、horizon、母體及異常口徑下高報酬／低報酬列的特徵，不以勝率單獨調參。沿用描述分組 high>=10%、low<=-10%、middle=(-10%,10%)；negative<0% 仍是獨立 failure 指標，此分組不構成任何策略 gate。特徵對照的排除敏感度僅用不可變的既有候選，不以新全期候選選參數。
報告樣本數、win/neutral/failure、平均／中位實現價格報酬、>=10% 命中率、<=-10% 損失率及包含／排除候選的數字。
異常候選保留 primary；排除只能標示 sensitivity，不能稱 corrected performance。保留既有 annual／horizon／condition 三份固定候選來源，按 signal_date／stock_id／horizon 精確匹配，不跨 horizon；未被本次交易代表者只列來源證據與計數，不生成假交易。新增候選沿用每個 profile／strategy／horizon 完整時序（含 purged_cross_split）成熟 10bps 帳本，以 `statistics.quantiles(n=4,method="inclusive")` 計 Q1/Q3，嚴格落在 Q1−3IQR／Q3+3IQR 外才列候選；不足四列不產生新 IQR 候選，不逐 train/validation 分開估界。候選鍵於本次各帳本取聯集並同步三成本情境，保留原判定帳本與邊界來源。公司行動、調整基礎與原始可得性未核實，不能支持 promotion。
400+ 與 1000+ 是重疊級距，無法證明同一批大戶持續買進。
月營收，以及 EPS、毛利率、營益率、營業利益、業外損益、淨利、季度／年度財報欄位全部排除。

## 最小回歸與獨立驗證

- 不等日期 `p=30+d/7` 應為 1 pp/week。
- 等距八批 400=`40+[1,2,3,4,5,6,7,0]`、1000=`20+[1,2,3,4,5,6,7,0]`，slope 都為 +1/3；末四批淨變化負，新式仍接受。
- 常數，以及等距日期上的 `[1,2,3,4,4,3,2,1]` slope 恰為 0，拒絕。同一對稱比例搭配 `d=[0,7,14,21,28,35,42,48]` 則 slope=`84/16079>0`，不得按比例序列對稱強制歸零。
- 6／8 日間隔不誤判缺週，完整休市週與缺開市週分開驗證。
- 缺當期一批不能回補舊批；future TDCC mutation 不得改過去 features。`signal_date=20251016` 不因未來 `20251017` 批被移除／修改而改變資格。
- 共同起點空倉、跨 split 不 reset、entry-date split 與 purged lock 各有回歸。
- 獨立 validator 不匯入本 producer 的業務判斷；重算 raw source、母體、斜率、交易、統計與文件披露。

本次研究數值尚未運算。總管已確認精確新 owner／producer mapping 與新路徑屬本次必要登錄；只新增封閉登錄，不改 workflow、不放寬未知 writer、不減少既有 annual 檢查。
