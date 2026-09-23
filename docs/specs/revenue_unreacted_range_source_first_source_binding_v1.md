# 營收爆發但股價尚未反應模型：來源優先研究版本綁定 v1

授權參照：`user_approved_revenue_source_version_binding_repair_20260923`。

## 範圍

本修復只固定 `revenue_unreacted_range` 已發布來源優先研究的來源與產物版本，
不重算、不替換舊研究證據。模型條件、評分、排序、買賣與回測規則、
正式 adapter、readiness、六份 PDF、workflow 與 Apps Script 均不修改。
範圍僅月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利及季度／年度財報均不納入。

## 固定證據

`config/revenue_unreacted_range_source_first_source_binding.csv` 恰含八列：
月營收歷史與跨市場 resolution 兩件來源，以及既有 summary、detail、markdown、
history summary、docs summary、docs markdown 六件研究產物。
來源提交固定為 `0a7044debe9dbdae01b4e30910aec3d595ef4edf`；
研究版本仍為 `source_first_condition_v3_20260720`。
每件綁定路徑、Git 物件與內容雜湊必須相符；缺件、錯誤版本或內容變更 fail closed。
Git 固定來源的完整內容必須可取得，不能以 mutable latest 或只保留部分來源列替代。

舊 source snapshot projection v2、`20260713` cutoff 及下游研究鏈不變。
本次不是新的 PIT 宣稱、獨立回測重跑或正式升級證據。

## 驗證與最新資料分流

`scripts/validate_revenue_unreacted_range_source_first_source_binding.py`
獨立驗證固定來源與六件產物，不 import producer 的模型條件或商業函式。
它可使用既有獨立 projection validator 的純來源正規化與雜湊函式，
但不改寫 projection 或繞過來源列身分與 lineage 驗證。

`scripts/validate_revenue_unreacted_range_source_first_condition_audit.py`
繼續檢查研究結構與既有 cutoff；固定版本的完整來源與逐列雜湊是硬性檢查，
current 來源則另作差異揭露。新增後期月營收不要求覆寫既有研究，
但 current cutoff 內的內容變更仍阻擋。transport byte 差異不能取代 canonical 檢查。

## 執行與保留

`scripts/build_revenue_unreacted_range_research.py` 的
`source_first_condition_audit` 與 `all` 路徑驗證並保留六件固定研究，
明確回報 `retained_frozen_source_evidence`，不以最新來源無聲覆寫舊證據。
既有核心研究計算不變；直接 writer 必須在任何寫入之前拒絕變更固定產物。
排程的 projection-chain 與 forward-holdout 路徑保持原有行為。

研究 workflow 的 shallow checkout 不保證含有固定來源提交。只有需要本綁定的
model-owned CLI 階段可先檢查 Git 物件；固定提交已存在時不連線，僅在 shallow
且缺少該提交時以 `--no-tags --depth=1 --no-write-fetch-head` 取回精確 full SHA。
不得 checkout、移動分支、改寫工作檔案或改用 mutable latest；失敗即停止。
獨立 validator 本身不執行 fetch，仍須有完整指定來源物件才能通過。

`tests/test_revenue_unreacted_range_source_first_source_binding.py`
涵蓋來源／產物變更、缺件與版本綁定回歸；經既有來源優先測試入口執行，
不新增 workflow。登錄檔同步維持單一模型所有權與 append-only migration；
必要的 model-data independence audit 鏡像不屬於重算研究成果。
