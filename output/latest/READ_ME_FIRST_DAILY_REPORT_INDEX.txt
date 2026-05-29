generated_at=2026-05-29 19:34:50 Asia/Taipei
main_price_date=20260529
report_ready=True
commit_sha=e8dc8789f86aef263abf647ee98b42b21c77782e
latest_readme_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT.txt
latest_readme_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT.txt
latest_readme_github_api_url=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/READ_ME_FIRST_DAILY_REPORT.txt?ref=main
date_stamped_readme_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT_20260529.txt
date_stamped_readme_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT_20260529.txt
date_stamped_readme_github_api_url=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/READ_ME_FIRST_DAILY_REPORT_20260529.txt?ref=main
history_readme_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/history/reports/20260529_READ_ME_FIRST_DAILY_REPORT.txt
history_readme_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/history/reports/20260529_READ_ME_FIRST_DAILY_REPORT.txt
astrology_read_protocol_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/astrology_read_protocol_latest.md
astrology_read_protocol_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/astrology_read_protocol_latest.md
preferred_chatgpt_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/chatgpt_daily_report_packet_latest.txt
recommended_read_order=astrology_read_protocol_pages_url only for Zi Wei / Ba Zi / astrology tasks,astrology_read_protocol_raw_url only for Zi Wei / Ba Zi / astrology tasks,date_stamped_readme_pages_url,date_stamped_readme_raw_url,date_stamped_readme_github_api_url,history_readme_pages_url,history_readme_raw_url,latest_readme_pages_url,latest_readme_raw_url,latest_readme_github_api_url
daily_task_fallback_rule=If latest_readme_* returns an older main_price_date, do not stop. Try the date-stamped README for the expected Taiwan trading date. If that fails, try the previous 7 calendar dates through raw and GitHub API. Use only a report_ready=True entry and state the actual main_price_date used.

RULES:
1. Prefer date-stamped README URLs over latest URLs when a daily task expects a specific date.
2. If latest is stale, try the expected YYYYMMDD date-stamped README, then previous 7 calendar dates.
3. GitHub API contents URLs must be base64 decoded before parsing key=value.
4. Never use an old main_price_date as a newer-date report.