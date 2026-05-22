main_price_date=20260523
report_ready=True
commit_sha=fea1751d28fff3cae9e735044ebf8941ed756e33
preferred_chatgpt_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/fea1751d28fff3cae9e735044ebf8941ed756e33/output/history/reports/20260523_CHATGPT_DAILY_REPORT_PACKET.txt
packet_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/chatgpt_daily_report_packet_latest.txt
packet_commit_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/fea1751d28fff3cae9e735044ebf8941ed756e33/output/history/reports/20260523_CHATGPT_DAILY_REPORT_PACKET.txt
packet_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/chatgpt_daily_report_packet_latest.txt
packet_github_api_url=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/chatgpt_daily_report_packet_latest.txt?ref=main
summary_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_summary_latest.md
full_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_full_latest.md
packet_pages_ok=False
packet_commit_raw_ok=True
packet_latest_raw_ok=True
packet_github_api_ok=True
read_order=packet_pages_url,packet_commit_raw_url,packet_latest_raw_url,packet_github_api_url

RULES:
1. Read preferred_chatgpt_url first.
2. If preferred_chatgpt_url fails, follow read_order.
3. If the URL is packet_github_api_url, decode the JSON content field from base64 before reading the packet.
4. If packet is readable, use EMBEDDED SUMMARY REPORT and EMBEDDED FULL REPORT as source of truth.
5. If all URLs fail, say tool reading failed. Do not say GitHub data is not updated.
6. Do not use older report dates to recreate a newer report.
