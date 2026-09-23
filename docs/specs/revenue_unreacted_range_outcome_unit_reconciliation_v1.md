# 營收爆發但股價尚未反應：凍結 v3 公司行動單位校準

授權：`user_authorized_all_requested_model_owned_corporate_action_research_repairs_20260923`。

獨立 model-owned local-only producer：
`python scripts/build_revenue_unreacted_range_outcome_unit_reconciliation.py`。
既有 wrapper、workflow、price resolution、selector、正式 adapter/readiness、六份 PDF 與舊研究產物不變。

讀取 `001b82f856c4ca1a863d64998890fb1fdfba8030` 的六份凍結 v3，價格與舊 resolution
固定 `231d2e279a99a89f1888ece0361ea64d45f69ecd`，不 fetch、不 checkout 或落地整批原始行情。
20,430 個 episode 與原始欄位均保留。D20 是原有個股有效 close 序列加20；停牌不占有效序列。
不改 first_breakout/launch 日期、不重算條件、特徵、episode_status、launch 或啟動率。

只對 D0 < 換股生效日 <= D20 的官方核實事件，將既有分析價格 outcome 加上尚未反映的持股單位倍率。
既有3593／2380 normalization先獨立重現原outcome，與新增事件重疊時停止，禁止double adjustment。
4763於20250630每1舊股換10新股；20250522收893至20250701收90.8的單位校準觀察為約+1.679731%，
不是含股利／費稅的總報酬或正式操作損益。原有異常旗標不清除；全部列保留primary。

證據為config內model-owned的完整官方response text UTF8 base64、exact bytes SHA256及正文識別token；
不是HTTP transport wire bytes，目前取得的版本不是首次發布PIT，也未證明原始更正鏈。
新config與六產物以canonical JSON或UTF8無BOM LF bytes綁定；產物與程式容許checkout的首BOM/CRLF transport正規化，
原Git blob／receipt仍嚴格raw bytes。producer guard保護Git tree/index與存在實體的SHA，不宣稱稀疏缺檔已實體驗證。

唯一新輸出前綴 `output/research/revenue_unreacted_range/revenue_unreacted_range_outcome_unit_reconciliation_v1_20260923_`，
精確六檔：manifest.json、detail.csv、actions.csv、comparison.csv、changes.csv、report.md。舊證據不可覆寫。

獨立validator：`python scripts/validate_revenue_unreacted_range_outcome_unit_reconciliation.py`。
它不匯入producer或production業務函式，驗證原列、日期、raw/normalized價格、換股倍率、明細與彙總、lineage與false flags。
primary保留所有未解候選；敏感度排除不是修正績效。尚茂8291來源量額疑點不在模型內修補。

僅月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利及季／年財報排除。
全部formal、promotion、PDF、production旗標false；尚未證實完整公司行動、現金流、交易日曆、可成交性與首次發布PIT。
