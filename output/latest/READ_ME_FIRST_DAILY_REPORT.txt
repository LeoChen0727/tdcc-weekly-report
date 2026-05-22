DAILY MARKET REPORT READ ME FIRST

generated_at: 2026-05-22 23:10:03 Asia/Taipei
repo: LeoChen0727/tdcc-weekly-report
main_price_date: 20260522
report_ready: True

IMPORTANT RULES FOR CHATGPT READER

1. This file is the first file to read before producing the daily Taiwan stock candidate report.
2. If this file says report_ready=True and main_price_date is the target report date, GitHub has produced the official report.
3. If the report files below cannot be read, say the reading tool failed. Do NOT say GitHub data is not updated.
4. Do NOT reuse older reports such as 20260521 to recreate a newer report such as 20260522.
5. Prefer English alias filenames first. Avoid relying on Chinese filenames when the reader tool has cache issues.
6. If MD files fail, try PDF files. If both fail, ask the user to upload the MD/PDF files.

PRIMARY FILES TO READ IN ORDER

- report_manifest_latest.md
  path: output/latest/report_manifest_latest.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/report_manifest_latest.md
- report_manifest_latest.json
  path: output/latest/report_manifest_latest.json
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/report_manifest_latest.json
- data_freshness_latest.md
  path: output/latest/data_freshness_latest.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/data_freshness_latest.md
- daily_market_summary_latest.md
  path: output/latest/daily_market_summary_latest.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_summary_latest.md
- daily_market_full_latest.md
  path: output/latest/daily_market_full_latest.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_full_latest.md
- daily_market_summary_latest.pdf
  path: output/latest/daily_market_summary_latest.pdf
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_summary_latest.pdf
- daily_market_full_latest.pdf
  path: output/latest/daily_market_full_latest.pdf
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_full_latest.pdf

SECONDARY DATA FILES

- all_candidates_latest.csv
  path: output/latest/all_candidates_latest.csv
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/all_candidates_latest.csv
- all_candidates_latest.xlsx
  path: output/latest/all_candidates_latest.xlsx
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/all_candidates_latest.xlsx
- chart_manifest.csv
  path: output/latest/chart_manifest.csv
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/chart_manifest.csv
- contact_sheet_manifest.csv
  path: output/latest/contact_sheet_manifest.csv
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/contact_sheet_manifest.csv
- official_price_fetch_latest.md
  path: output/latest/official_price_fetch_latest.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/official_price_fetch_latest.md
- official_price_fetch_latest.json
  path: output/latest/official_price_fetch_latest.json
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/official_price_fetch_latest.json
- warrant_flow_latest.csv
  path: output/latest/warrant_flow_latest.csv
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/warrant_flow_latest.csv
- stock_monitor_latest.md
  path: output/latest/stock_monitor_latest.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/stock_monitor_latest.md

CHINESE DISPLAY FILES

- 每日全市場候選股監測報告_精華版.md
  path: output/latest/每日全市場候選股監測報告_精華版.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/每日全市場候選股監測報告_精華版.md
- 每日全市場候選股監測報告_精華版.pdf
  path: output/latest/每日全市場候選股監測報告_精華版.pdf
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/每日全市場候選股監測報告_精華版.pdf
- 完整候選股清單_完整版.md
  path: output/latest/完整候選股清單_完整版.md
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/完整候選股清單_完整版.md
- 完整候選股清單_完整版表格.pdf
  path: output/latest/完整候選股清單_完整版表格.pdf
  status: exists
  raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/完整候選股清單_完整版表格.pdf

DATE CHECK

main_price_date: 20260522
report_ready: True
all_candidates_date: 20260522
official_price_fetch_date: 20260522
stock_monitor_date: 20260522
warrant_flow_date: 20260522

EXPECTED BEHAVIOR

If main_price_date matches the requested date and report_ready=True:
- Produce the report from daily_market_summary_latest.md and daily_market_full_latest.md when readable.
- If these files cannot be read due to Cache miss, report a tool-reading failure.
- Do not claim the GitHub report has not been produced.
- Do not use stale older files to recreate today's report.
