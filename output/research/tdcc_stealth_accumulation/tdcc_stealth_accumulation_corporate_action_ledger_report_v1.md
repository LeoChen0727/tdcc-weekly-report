# TDCC 潛伏吸籌：公司行動研究帳本 v1

這是固定四股的事後帳務補證，不是選股重算、修正勝率或正式模型升級。

來源：3fe40157cf4b333ef03a1447e45c310d197cbc5b；截止日 20260909。保留 59 個來源訊號、90 列原研究交易情境與 381 列原阻擋紀錄。

交易情境含 0／10／20 bps 三種滑價，共 90 列；10 bps 為 30 個各持有期部位，不同持有期不能當成互相獨立實驗。已知事件涉及 15 列情境；未匹配事件不等於證明沒有其他事件。

| 股票 | 已知事件與帳務界線 |
|---|---|
| 強生 4747 | 1 股換 2 股；8/20～8/28 停牌，8/31 新股恢復交易。只核對理論股數，不推定其他公司行動已完整查核。 |
| 青雲 5386 | 7/20 取得配股／股息權利；每仟股 500.00001386 股、每股現金 1.5 元。8/14 新股權利證書才可交易；原 7/22／8/5 出場不能賣出未到手權利。 |
| 益得 6461 | 減資後每仟股換 618.578 股，9/9 復牌；每股退還股款 0。整股／小數只是數學組成，不假設畸零股合併、出售或現金入帳。 |
| 緯穎 6669 | 每仟股配發 1982.79460 股，9/2 除權；交付／可交易日未取得，保留待交付權利。9/16～9/30 認購繳款期不是交付日期。 |

`known_event_share_balance` 是僅套用已列事件的理論股數；`eligible_whole_share_component`／`unresolved_fractional_share_component` 是算術拆分，不是已成交或已入帳證明。`pending_share_rights` 與 `unsettled_gross_cash_entitlement` 分開；公告付款日不是實收證據。沒有現金確認證據時 `confirmed_cash_receipt` 空白，不填零冒充已核實。

原定 D+5／D+10／D+20 出場日、原訊號及持倉鎖不變。未到帳權利不假造價格、不延長賣出日、不計已實現收益。舊 proxy 報酬僅保留於 `original_proxy_net_return_pct`，不得稱為修正績效。所有 `verified_total_return_pct` 空白，`total_return_verified=False`；沒有正式勝率分母。

官方原件取回在事件之後，只供 retrospective reconciliation，不作 signal PIT 證據。未建立完整公司行動覆蓋、個別實收／畸零股證明，也沒有補回 21 個既有版本收據缺口。異常候選保留原列、不作最終 disposition 或剔除。

五個模型專屬產物以 source_manifest 綁定最終 bytes SHA-256；契約內封存官方原件及固定 Git 來源。獨立 validator 不匯入 producer 商業邏輯。研究仍 `formal_use=False`、`promotion_evidence_allowed=False`；其他模型、舊產物、六份 PDF、Apps Script、月營收及 EPS 等季度／年度財報均不變。
