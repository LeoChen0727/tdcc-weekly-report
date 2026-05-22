main_price_date=20260523
report_ready=True
commit_sha=14c1dee8f88c0c2ad4518b16d09f2194cb83ba26
preferred_chatgpt_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/chatgpt_daily_report_packet_latest.txt
packet_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/chatgpt_daily_report_packet_latest.txt
packet_commit_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/14c1dee8f88c0c2ad4518b16d09f2194cb83ba26/output/history/reports/20260523_CHATGPT_DAILY_REPORT_PACKET.txt
summary_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_summary_latest.md
full_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_full_latest.md
packet_latest_raw_ok=True
packet_commit_raw_ok=True

RULES:
1. Read preferred_chatgpt_url first.
2. If preferred_chatgpt_url fails, try packet_commit_raw_url, then packet_latest_raw_url.
3. If packet is readable, use EMBEDDED SUMMARY REPORT and EMBEDDED FULL REPORT as source of truth.
4. If GitHub raw reading fails, say tool reading failed. Do not say GitHub data is not updated.
5. Do not use older report dates to recreate a newer report.
