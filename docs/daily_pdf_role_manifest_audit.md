# Daily PDF Role / Manifest Audit

日期：2026-07-06

Owner lane：`daily_model_maintenance / model_governance`

## 結論

六份 ChatGPT-side daily PDF 的正式角色來源必須是 runtime manifest 裡的 `pdf_role`，不是檔名、中文標題、substring 或 PDF 文字標題。

本 audit 確認並加固以下 contract：

1. `scripts/run_chatgpt_daily_report_entrypoint.py` 是 `pdf_role` manifest 的 owner。
2. `scripts/validate_chatgpt_daily_report_new_conversation_replay.py` 必須從 `chatgpt_daily_report_runtime_manifest.json` 的 `pdf_outputs` 讀取 `pdf_role` 對應 PDF path。
3. highlight layout 與 rendered model regression 都只能透過 `pdf_role` 取得 PDF text，不能從檔名或中文 title 反推角色。
4. PDF filename 只允許用來檢查日期、輸出目錄、stale residue 與 `_current_rules.pdf` 後綴，不允許用來做 role matching。

## 六份正式角色

| pdf_role | PDF 語意 |
| --- | --- |
| `mainstream_highlight` | 主流股每日推薦精華 |
| `mainstream_full` | 主流完整候選清單 |
| `non_mainstream_highlight` | 非主流股每日推薦精華 |
| `non_mainstream_full` | 非主流完整候選清單 |
| `warrant_market_auxiliary` | 權證 / 市場輔助分析 |
| `market_risk_background` | 大盤風險與市場背景 |

## 已確認的風險

過去 substring 問題的根因是用檔名或中文 title token 判斷 role 時，`非主流` 會包含 `主流`，造成主流 / 非主流 PDF 被誤配或覆蓋。這類問題不能靠人工看檔名避免，必須由 validator 禁止 role/title substring mapping。

本 PR 移除 replay validator 的 title-driven remnants：

- `EXPECTED_TITLES`
- `HIGHLIGHT_LAYOUT_TITLES`
- `HIGHLIGHT_LAYOUT_ROLE_TITLES`
- `title_to_pages`

## Validator contract

`scripts/validate_daily_pdf_role_manifest_contract.py` 必須 fail closed：

- entrypoint 的 `PDF_OUTPUT_ROLES` 必須固定為六個正式 role。
- runtime manifest 必須提供 `pdf_outputs`，每個 item 必須有 `pdf_role`、`pdf_index`、`path`。
- replay validator 的 highlight layout 與 rendered model regression 必須呼叫 `role_to_pdf_paths_from_manifest()`。
- replay validator 不得包含 title-token matching remnants。
- regression contract 的 `pdf_role` 必須屬於六個正式 role。
- workflow 必須呼叫 `python scripts/validate_daily_pdf_role_manifest_contract.py`。

## 邊界

本 audit 不變更任何股票模型條件、scoring、ranking、PDF 版型或 candidate selection。

本 audit 不處理第二階段 golden regression 擴大，也不處理 shared path 拆分；那些屬於後續獨立 PR。
