# Catalyst Needs Review

- generated_at: `2026-06-15 21:25:12 Asia/Taipei`
- rows: `2`
- policy: Rows in this table are not confirmed catalyst data.
- model_effect_allowed: `False` means the item cannot affect score, rank, upgrade, downgrade, or similar_to_shihsinko_flag.
- pdf_effect_allowed: `False` means the item cannot appear as a formal recommendation reason in the PDF.

## Data-Source Priority

1. Use original structured data first: CSV, packet fields, source logs, signal logs, warrant tables, market tables, and validated raw links.
2. Use Markdown/PDF reports only as auxiliary readable summaries.
3. If raw/source tables cannot be read and only PDF content is used, the report must start by saying: `本次僅使用 PDF 報告資料，未讀取原始 CSV / packet / source tables，因此只能做摘要型分析。`

## Items Pending Source Confirmation

| item_id | source_area | requested_data | current_status | owner | model_effect_allowed | pdf_effect_allowed | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mops_shareholder_meeting_calendar | company_calendar | Stock-level shareholder meeting dates | partial_coverage_twse_only | codex_data_source_work | False | False | Keep TWSE OpenAPI rows; find and test a stable MOPS/TPEX endpoint before claimin... |
| company_specific_event_sources | event_catalyst | Company-specific technology validation, exhibitions, news, investor conference, ... | partial_official_material_info_rows | program_auto_confirm_after_source_integration | False | False | Broaden beyond official material-information rows to company releases, exhibitio... |
