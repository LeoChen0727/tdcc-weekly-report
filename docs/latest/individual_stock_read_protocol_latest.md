# Individual Stock Raw Data Read Protocol

- generated_at: 2026-05-26 03:10:29 Asia/Taipei
- scope: every Taiwan stock id with repo raw data
- individual_report_md_is_optional: True
- individual_stock_chatgpt_packet_is_primary_read_entry: True
- price_and_tdcc_raw_are_primary_source_tables: True

## Core Rule

For any `stock_id`, use the same fixed packet-first, raw-data-backed flow. Do not require `output/latest/individual_stock_reports/{stock_id}_latest.md` to exist before analysis.

## Universal URL Templates

| logical_source | first_url | fallback_url | final_fallback |
| --- | --- | --- | --- |
| individual_chatgpt_packet | `https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md` | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md` | GitHub API contents + base64 decode |
| price_window_180_html | `https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html` | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html` | GitHub API contents + base64 decode |
| price_window_180_txt | `https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt` | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt` | GitHub API contents + base64 decode |
| price_history | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/{stock_id}.csv?ref=main` | decode GitHub API JSON `content` from base64 |
| tdcc_history | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/{stock_id}.csv` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/{stock_id}.csv?ref=main` | decode GitHub API JSON `content` from base64 |
| individual_report_md_optional | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/{stock_id}_latest.md` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.md?ref=main` | if missing, continue with raw price / TDCC |
| individual_report_json_optional | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.json?ref=main` | none | optional convenience only |

## Recommended Fixed Flow

1. Normalize stock id to four digits when applicable.
2. Read the individual ChatGPT packet first. It gives stable URLs, latest snapshot, recent TDCC rows, candidate context, repeat appearance, and warrant context.
3. For any K-line, MA, volume, support/resistance, or pattern conclusion, always read `price_window_180_html` first. The 20-row packet preview is not enough for technical analysis.
4. If packet/raw/pages returns Cache miss, Internal Error, stale content, or `Total lines: 1`, read the matching GitHub API URL and base64-decode `content`.
5. Use full price / TDCC raw CSV only for programmatic backtests or extra columns. Do not require ChatGPT to expand full raw CSV before ordinary single-stock analysis.
6. If raw price history returns Cache miss, Internal Error, stale content, or `Total lines: 1` while the file is expected to be multi-line, use the `price_window_180_html` or GitHub API fallback before downgrading the report.
7. If price rows >= 60, the stock can be analyzed as `standard_rawdata_report` even when the individual Markdown/PDF report does not exist.
8. Read TDCC history from the packet first, then TDCC raw/API fallback if needed.
9. If TDCC rows < 8 weekly rows, mark `insufficient_tdcc_history`; do not make 8-12 week TDCC backtest conclusions.
10. Read individual report Markdown only as an optional prepared report. If it is missing, continue with packet/raw data.
11. External websites may supplement news, announcements, broker targets, or events, but must not replace repo price history or repo TDCC history as primary data.

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

If a prepared individual report is missing, do not say the repo lacks data. Read `individual_stock_chatgpt_packets/{stock_id}_packet_latest.md` first. If packet/raw URLs fail, use GitHub API contents and base64 decode. Only after packet and price raw/API both fail should the report be downgraded to event-only or insufficient-data.
