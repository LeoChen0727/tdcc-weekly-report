main_price_date=20260524
report_ready=True
commit_sha=5658e631664cdeb60463e92a93d355b195409214
preferred_chatgpt_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/chatgpt_daily_report_packet_latest.txt
packet_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/chatgpt_daily_report_packet_latest.txt
packet_commit_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/5658e631664cdeb60463e92a93d355b195409214/output/history/reports/20260524_CHATGPT_DAILY_REPORT_PACKET.txt
packet_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/chatgpt_daily_report_packet_latest.txt
packet_github_api_url=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/chatgpt_daily_report_packet_latest.txt?ref=main
summary_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_summary_latest.md
full_latest_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_full_latest.md
daily_market_curated_pdf_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/daily_market_curated_report_latest.pdf
daily_market_curated_pdf_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_curated_report_latest.pdf
daily_market_full_table_pdf_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/daily_market_full_table_report_latest.pdf
daily_market_full_table_pdf_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_full_table_report_latest.pdf
fixed_pdf_validation_status=pass
fixed_pdf_validation_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_market_report_validation_latest.md
pdf_kline_status_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/pdf_kline_chart_status_latest.md
pdf_kline_status_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/pdf_kline_chart_status_latest.md
summary_pdf_kline_policy=local_price_redraw_first
summary_pdf_kline_status=generated
summary_pdf_kline_total_charts=20
summary_pdf_kline_local_price_redraw_count=20
summary_pdf_chart_path_and_chart_url_are_fallback_only=True
do_not_label_summary_pdf_as_chart_path_version_or_image_download_failed=True
daily_signal_performance_summary_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_signal_performance_summary_latest.md
daily_signal_performance_weekly_md_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_signal_performance_weekly_latest.md
daily_signal_performance_weekly_pdf_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/daily_signal_performance_weekly_latest.pdf
daily_signal_performance_weekly_pdf_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_signal_performance_weekly_latest.pdf
daily_signal_performance_monthly_md_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_signal_performance_monthly_latest.md
daily_signal_performance_monthly_pdf_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/daily_signal_performance_monthly_latest.pdf
daily_signal_performance_monthly_pdf_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/daily_signal_performance_monthly_latest.pdf
warrant_market_report_md_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/warrant_market_report_latest.md
warrant_market_report_pdf_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/warrant_market_report_latest.pdf
warrant_market_report_pdf_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/warrant_market_report_latest.pdf
warrant_flow_by_stock_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/warrant_flow_by_stock_latest.csv
warrant_sector_heat_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/warrant_sector_heat_latest.csv
warrant_signal_performance_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/warrant_signal_performance_latest.md
market_regime_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/market_regime_latest.csv
market_risk_dashboard_md_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/market_risk_dashboard_latest.md
market_risk_dashboard_pdf_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/market_risk_dashboard_latest.pdf
market_risk_dashboard_pdf_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/market_risk_dashboard_latest.pdf
futures_options_indicators_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/futures_options_indicators_latest.csv
futures_options_source_status_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/futures_options_source_status_latest.md
rules_pages_url=https://LeoChen0727.github.io/tdcc-weekly-report/latest/CHATGPT_DAILY_REPORT_RULES.txt
rules_raw_url=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/CHATGPT_DAILY_REPORT_RULES.txt
packet_pages_ok=True
packet_commit_raw_ok=True
packet_latest_raw_ok=True
packet_github_api_ok=True
read_order=packet_pages_url,packet_commit_raw_url,packet_latest_raw_url,packet_github_api_url

RULES:
1. Read this entry file first.
2. Read rules_pages_url or rules_raw_url to load report format rules.
3. Read preferred_chatgpt_url for the packet.
4. If preferred_chatgpt_url fails, follow read_order.
5. If the URL is packet_github_api_url, decode the JSON content field from base64 before reading the packet.
6. If packet is readable, use EMBEDDED SUMMARY REPORT and EMBEDDED FULL REPORT as source of truth.
7. For shareable PDFs, use daily_market_curated_pdf_pages_url and daily_market_full_table_pdf_pages_url first.
8. For the summary PDF K-line charts, use summary_pdf_kline_policy/status/counts above. Do not downgrade the PDF to chart_path/image-download-failed if local_price_redraw_count is greater than 0.
9. If all URLs fail, say tool reading failed. Do not say GitHub data is not updated.
10. Do not use older report dates to recreate a newer report.
