# 營收爆發但股價尚未反應模型：行情版本綁定與 v3 差異稽核

授權：`user_approved_revenue_projection_price_binding_v3_diff_20260923`。
本次只處理月營收研究的行情資料版本，不變更條件、評分、排序、買賣規則、正式 adapter、readiness、六份 PDF 或 Apps Script。
EPS、毛利率、營益率、營業利益、業外損益、淨利及季度／年度財報不在範圍。

## 舊證據

`source_snapshot_projection_v2_20260822` 的固定來源 ref 為
`4bcaa07123ef4a000c187dc2f19caefbec4cf252`。此提交的 1,972 股、475,067 筆
cutoff 內行情及逐股 semantic SHA 與既有 manifest 相同；它是明確選定的不可變來源，
不是宣稱歷史執行時唯一的 HEAD。其 parent 及後續 canonical supersede 的來源內容相同。

原 v1、v2、v1-v2 diff、supersede evidence、canonical latest 及下游研究產物全部保持原 bytes。
舊 projection 與四個直接重讀價格的研究 validator 改讀固定來源中的完整 raw price
及 price resolution，再照原公式與 cutoff 重播。獨立 validator 不匯入 producer 的業務計算。
月營收的 current cutoff gate 保留；新日資料正常追加不會被誤稱歷史行情毀損。

## 新候選

唯一 producer：`scripts/build_revenue_unreacted_range_projection_v3.py`。
新來源固定為 `231d2e279a99a89f1888ece0361ea64d45f69ecd`，觀察截止日仍為 `20260713`。
新、舊 cutoff 月營收 semantic identity 必須相同，兩份 resolution registry 不得改變；
不符即停止價格單因子比較。原條件與事件算法直接重用同模型既有 producer，僅增加記憶體 bytes IO。

只可產生以下六份新版本檔案，共同目錄為 `output/research/revenue_unreacted_range/`，
共同前綴為 `revenue_unreacted_range_source_snapshot_projection_v3_20260923_`：

- `manifest.csv`：固定來源 commit、tree、raw source SHA、v2 原始證據 SHA、其餘五件產物 SHA。
- `detail.csv`：維持 source-first row schema 的 v3 候選事件明細；由新 manifest 綁定。
- `price_diff.csv`：全體 cutoff 股票的價格列數、semantic SHA、新增／移除日期及共同日期值變動。
- `episode_diff.csv`：全部新增、移除或語意改變的 episode key 與欄位名；不隱藏 sequence index 差異。
- `comparison.csv`：同條件的兩版本主要統計及明確分離的候選排除敏感度。
- `report.md`：繁體中文結果與使用邊界。

新版產物 SHA 綁定 producer 的 UTF-8、無 BOM、LF 序列化 bytes；驗證只允許 checkout
造成的首個 UTF-8 BOM 與 CRLF transport 差異，不修剪或變更 CSV 值。固定 Git 原始來源
及舊 v2 blob 仍依原始 bytes 查核，不做此 transport 正規化。

既有檔案不得覆寫；不得寫入 canonical latest 或其他模型。Producer 在計算前確認精確
ownership allowlist，並以 Git tree/index 與現存實體 SHA 保護正式 sentinel。Sparse 缺少的
實體檔案只聲稱 Git identity 保護，不聲稱已實體檢查；不展開受保護資料目錄。

補入歷史日期不代表當時可取得該版本，故新候選是固定 current-version replay，
不是首次發布版本的嚴格 PIT 證據。回溯啟動率與 D20 收盤觀察不等於正式操作勝率。
未解異常候選保留主要統計；排除結果只作敏感度，數值大小不能單獨證成資料錯誤。
所有 formal、promotion、PDF、production flags 均為 false。採用新候選須另行決定。

## 驗證

`scripts/validate_revenue_unreacted_range_projection_v3.py` 獨立重播新來源、核對六件產物綁定、
價格與事件差異完整性、比較統計及研究專用旗標。唯讀 Git loader 不 checkout、不 fetch、
不落原始資料；缺少固定 commit 即明確失敗。現有官方 workflow 的 full-history checkout
提供來源版本，無 workflow 修改。
