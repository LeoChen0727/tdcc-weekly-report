# Codex Project Brief

## Repo Purpose

`tdcc-weekly-report` is a Taiwan stock market daily candidate monitoring system. It fetches official market data, builds full-market candidate lists, generates daily reports, and publishes ChatGPT-readable entry files through GitHub Pages and raw GitHub URLs.

## Daily Full Pipeline

The main workflow is `.github/workflows/daily_full_pipeline.yml`.

At a high level, it:

1. Fetches official daily price data.
2. Runs full-market stock monitoring.
3. Builds candidate categories and all-candidates outputs.
4. Generates candidate charts, report artifacts, PDFs, packet files, and freshness checks.
5. Publishes GitHub Pages copies for ChatGPT entry points.
6. Checks multiple URLs so ChatGPT can read the latest report through more than one route.

## ChatGPT Multi-Entry Reading Flow

The first file to read is:

- GitHub Pages: `https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT.txt`
- Raw fallback: `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT.txt`

`READ_ME_FIRST_DAILY_REPORT.txt` provides key-value fields such as `main_price_date`, `report_ready`, `preferred_chatgpt_url`, packet URLs, and read order.

The packet can be read from:

- GitHub Pages packet URL
- Commit-specific raw URL
- Latest raw URL
- GitHub Contents API URL

When the GitHub Contents API is used, the JSON `content` field must be base64-decoded before reading the packet text.

## Important Output Files

- `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`
- `docs/latest/READ_ME_FIRST_DAILY_REPORT.txt`
- `output/latest/chatgpt_daily_report_packet_latest.txt`
- `docs/latest/chatgpt_daily_report_packet_latest.txt`
- `output/latest/chatgpt_daily_report_packet_manifest.json`
- `output/latest/report_publish_check_latest.md`
- `output/latest/report_publish_check_latest.json`
- `output/latest/daily_market_summary_latest.md`
- `output/latest/daily_market_summary_latest.pdf`
- `output/latest/daily_market_full_latest.md`
- `output/latest/daily_market_full_latest.pdf`
- `output/latest/all_candidates_latest.csv`
- `output/latest/all_candidates_latest.xlsx`
- `output/latest/all_candidates_latest.md`

## Files To Avoid Casual Edits

Do not modify these without a focused pipeline task:

- `.github/workflows/daily_full_pipeline.yml`
- `fetch_official_daily_price.py`
- `stock_daily_monitor.py`
- `build_all_candidates_latest.py`
- `build_daily_market_report_artifacts.py`
- Existing files under `output/latest/`
- Existing files under `output/history/`
- Existing files under `docs/latest/`

Do not remove the multi-entry reading mechanism:

- GitHub Pages
- Commit raw URL
- Latest raw URL
- GitHub Contents API

## Validation

For a documentation or Pages-only change:

1. Confirm only documentation or Pages files changed.
2. Open `docs/index.html` locally or through GitHub Pages after merge.
3. Open `docs/latest/index.html` locally or through GitHub Pages after merge.
4. Confirm the pages link to `READ_ME_FIRST_DAILY_REPORT.txt`, the report rules file, the ChatGPT packet, the summary PDF, the full PDF, and the publish check report.
5. Confirm `.github/workflows/daily_full_pipeline.yml` and core Python pipeline files are unchanged.
