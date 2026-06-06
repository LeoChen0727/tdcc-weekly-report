# Catalyst Needs Review

- generated_at: `2026-06-07 04:11:12 Asia/Taipei`
- rows: `4`
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
| mops_shareholder_meeting_calendar | company_calendar | Stock-level shareholder meeting dates | pending_endpoint_verification | codex_data_source_work | False | False | Find and test a stable MOPS endpoint before storing rows. |
| bls_cpi_release_schedule | macro_calendar | BLS CPI release schedule | reachable_not_parsed | codex_data_source_work | False | False | Build and validate parser before storing CPI/employment rows. |
| bls_employment_release_schedule | macro_calendar | BLS employment release schedule | reachable_not_parsed | codex_data_source_work | False | False | Build and validate parser before storing CPI/employment rows. |
| company_specific_event_sources | event_catalyst | Company-specific technology validation, exhibitions, news, investor conference, ... | needs_explicit_source_rows | program_auto_confirm_after_source_integration | False | False | Load explicit source rows from official announcements, MOPS, company releases, e... |
