# Daily Data Layer Consistency Audit

- status: `pass`
- main_price_date: `20260602`
- readme_main_price_date: `20260602`
- readme_index_main_price_date: `20260602`
- model_signal_rows: `846`
- volume_watch_rows: `1`
- volume_theme_other_rows: `0`
- group_rotation_rows: `13`
- taxonomy_rows: `2375`
- taxonomy_template_csv_rows: `2375`
- taxonomy_template_xlsx_rows: `2375`
- docs_taxonomy_template_csv_rows: `2375`
- docs_taxonomy_template_xlsx_rows: `2375`

## Errors

- none

## Warnings

- volume watch signal_date mismatch: expected 20260602, got ['20260529']; stale auxiliary table ignored for date gating

## Details

```json
{
  "main_price_date": "20260602",
  "readme_main_price_date": "20260602",
  "readme_report_ready": "True",
  "readme_index_main_price_date": "20260602",
  "readme_index_report_ready": "True",
  "effective_model_signal_date": "20260602",
  "model_signal_rows": 846,
  "raw_model_signal_rows": 846,
  "volume_watch_rows": 1,
  "volume_theme_stock_rows": 1,
  "group_rotation_rows": 13,
  "taxonomy_rows": 2375,
  "taxonomy_template_csv_rows": 2375,
  "taxonomy_template_xlsx_rows": 2375,
  "docs_taxonomy_template_csv_rows": 2375,
  "docs_taxonomy_template_xlsx_rows": 2375,
  "missing_required_model_columns": [],
  "blank_required_model_columns": {},
  "model_signal_dates": [
    "20260602"
  ],
  "same_model_report_duplicates": 0,
  "model_report_line_membership_mismatch_rows": 0,
  "model_signal_unreadable_text": {},
  "missing_model_display_columns": [],
  "model_signal_display_unreadable_text": {},
  "model_signal_display_raw_slug_rows": {},
  "model_signal_third_bucket_rows": {},
  "model_signal_main_condition_not_true_rows": 0,
  "raw_model_signal_dates": [
    "20260602"
  ],
  "missing_volume_columns": [],
  "volume_signal_dates": [
    "20260529"
  ],
  "volume_theme_other_rows": 0,
  "group_rotation_invalid_models": [],
  "group_rotation_slow_rows": 12,
  "group_rotation_launch_rows": 1,
  "missing_required_taxonomy_columns": [],
  "taxonomy_duplicate_stock_id_rows": 0,
  "taxonomy_unresolved_basic_theme_rows": 0,
  "taxonomy_unresolved_primary_theme_rows": 0,
  "taxonomy_third_bucket_rows": {},
  "taxonomy_blank_required_columns": {},
  "taxonomy_invalid_report_line_membership_rows": 0,
  "taxonomy_report_line_eligibility_mismatch_rows": 0,
  "taxonomy_sanity_errors": [],
  "taxonomy_template_missing_columns": [],
  "docs_taxonomy_template_missing_columns": []
}
```
