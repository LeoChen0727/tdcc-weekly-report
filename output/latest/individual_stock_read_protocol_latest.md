# Individual Stock Raw Data Read Protocol

- generated_at: 2026-05-26 01:30:37 Asia/Taipei
- scope: every Taiwan stock id with repo raw data
- individual_report_md_is_optional: True
- price_and_tdcc_raw_are_primary: True

## Core Rule

For any `stock_id`, use the same fixed raw-data-first flow. Do not require `output/latest/individual_stock_reports/{stock_id}_latest.md` to exist before analysis.

## Universal URL Templates

| logical_source | first_url | fallback_url | final_fallback |
| --- | --- | --- | --- |
| price_history | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/{stock_id}.csv?ref=main` | decode GitHub API JSON `content` from base64 |
| tdcc_history | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/{stock_id}.csv` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/{stock_id}.csv?ref=main` | decode GitHub API JSON `content` from base64 |
| individual_report_md_optional | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/{stock_id}_latest.md` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.md?ref=main` | if missing, continue with raw price / TDCC |
| individual_report_json_optional | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.json?ref=main` | none | optional convenience only |

## Recommended Fixed Flow

1. Normalize stock id to four digits when applicable.
2. Read price history from the price raw URL.
3. If raw price history returns Cache miss, Internal Error, stale content, or `Total lines: 1` while the file is expected to be multi-line, read the GitHub API price URL and base64-decode `content`.
4. If price rows >= 60, the stock can be analyzed as `standard_rawdata_report` even when the individual Markdown/PDF report does not exist.
5. Read TDCC history from the TDCC raw URL, then GitHub API fallback if needed.
6. If TDCC rows < 8 weekly rows, mark `insufficient_tdcc_history`; do not make 8-12 week TDCC backtest conclusions.
7. Read individual report Markdown only as an optional prepared report. If it is missing, continue with raw data.
8. External websites may supplement news, announcements, broker targets, or events, but must not replace repo price history or repo TDCC history as primary data.

## Status Definitions

| status | meaning |
| --- | --- |
| standard_rawdata_report | price raw data exists and has at least 60 rows |
| partial_rawdata_report | price raw data exists but is short, or supporting raw data is limited |
| insufficient_tdcc_history | TDCC history exists but has fewer than 8 weekly rows |
| individual_md_missing | prepared Markdown report is missing, but raw data may still support analysis |
| raw_fetch_failed | raw URL failed; try GitHub API contents fallback |
| content_not_expanded | URL opened but content did not expand into a usable table |

## ChatGPT Instruction

If a prepared individual report is missing, do not say the repo lacks data. Check `data/stock_price_history/{stock_id}.csv` and `data/tdcc_stock_history/{stock_id}.csv` first. If raw URLs fail, use GitHub API contents and base64 decode. Only after price raw and API both fail should the report be downgraded to event-only or insufficient-data.
