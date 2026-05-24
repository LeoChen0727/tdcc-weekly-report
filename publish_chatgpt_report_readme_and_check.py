from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import base64
import json
import os
import re
import subprocess
from typing import Any

import pandas as pd


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")
DOCS_LATEST_DIR = Path("docs/latest")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
PACKET_MANIFEST_JSON = LATEST_DIR / "chatgpt_daily_report_packet_manifest.json"
PDF_KLINE_STATUS_MD = LATEST_DIR / "pdf_kline_chart_status_latest.md"
PDF_KLINE_STATUS_JSON = LATEST_DIR / "pdf_kline_chart_status_latest.json"
DOCS_PDF_KLINE_STATUS_MD = DOCS_LATEST_DIR / "pdf_kline_chart_status_latest.md"
FIXED_PDF_MANIFEST_JSON = LATEST_DIR / "daily_market_pdf_report_manifest_latest.json"
FIXED_PDF_VALIDATION_MD = LATEST_DIR / "daily_market_report_validation_latest.md"
FIXED_PDF_VALIDATION_JSON = LATEST_DIR / "daily_market_report_validation_latest.json"
CURATED_REPORT_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_REPORT_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"
DOCS_CURATED_REPORT_PDF = DOCS_LATEST_DIR / "daily_market_curated_report_latest.pdf"
DOCS_FULL_TABLE_REPORT_PDF = DOCS_LATEST_DIR / "daily_market_full_table_report_latest.pdf"
DOCS_FIXED_PDF_VALIDATION_MD = DOCS_LATEST_DIR / "daily_market_report_validation_latest.md"

README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
DOCS_README_TXT = DOCS_LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"

PUBLISH_CHECK_MD = LATEST_DIR / "report_publish_check_latest.md"
PUBLISH_CHECK_JSON = LATEST_DIR / "report_publish_check_latest.json"

LATEST_PACKET = LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
DOCS_LATEST_PACKET = DOCS_LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"

RULES_LATEST = LATEST_DIR / "CHATGPT_DAILY_REPORT_RULES.txt"
RULES_DOCS = DOCS_LATEST_DIR / "CHATGPT_DAILY_REPORT_RULES.txt"

LATEST_SUMMARY_MD = LATEST_DIR / "daily_market_summary_latest.md"
LATEST_FULL_MD = LATEST_DIR / "daily_market_full_latest.md"
DAILY_SIGNAL_SUMMARY_MD = LATEST_DIR / "daily_signal_performance_summary_latest.md"
DAILY_SIGNAL_WEEKLY_MD = LATEST_DIR / "daily_signal_performance_weekly_latest.md"
DAILY_SIGNAL_WEEKLY_PDF = LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
DAILY_SIGNAL_MONTHLY_MD = LATEST_DIR / "daily_signal_performance_monthly_latest.md"
DAILY_SIGNAL_MONTHLY_PDF = LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"
DOCS_DAILY_SIGNAL_WEEKLY_PDF = DOCS_LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
DOCS_DAILY_SIGNAL_MONTHLY_PDF = DOCS_LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"
FUNDAMENTAL_CATALYST_MD = LATEST_DIR / "fundamental_catalyst_layer_latest.md"
WARRANT_MARKET_MD = LATEST_DIR / "warrant_market_report_latest.md"
WARRANT_MARKET_PDF = LATEST_DIR / "warrant_market_report_latest.pdf"
WARRANT_FLOW_BY_STOCK_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
WARRANT_SECTOR_HEAT_CSV = LATEST_DIR / "warrant_sector_heat_latest.csv"
WARRANT_SIGNAL_PERFORMANCE_MD = LATEST_DIR / "warrant_signal_performance_latest.md"
MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"
MARKET_RISK_DASHBOARD_MD = LATEST_DIR / "market_risk_dashboard_latest.md"
MARKET_RISK_DASHBOARD_PDF = LATEST_DIR / "market_risk_dashboard_latest.pdf"
FUTURES_OPTIONS_INDICATORS_CSV = LATEST_DIR / "futures_options_indicators_latest.csv"
FUTURES_OPTIONS_SOURCE_STATUS_MD = LATEST_DIR / "futures_options_source_status_latest.md"


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def now_text() -> str:
    return now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def normalize_date(value: Any) -> str:
    if value is None:
        return ""

    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass

    text = str(value).strip()
    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    return ""


def run_command(args: list[str], timeout: int = 40) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        return 124, exc.stdout or "", exc.stderr or "timeout"
    except Exception as exc:
        return 1, "", str(exc)


def raw_url(ref: str, path: Path) -> str:
    return f"{RAW_PREFIX}/{ref}/{path.as_posix()}"


def pages_url(path_under_docs: str) -> str:
    return f"{PAGES_PREFIX}/{path_under_docs.lstrip('/')}"


def github_api_url(path: Path, ref: str = "main") -> str:
    return f"https://api.github.com/repos/{OWNER_REPO}/contents/{path.as_posix()}?ref={ref}"


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    return {}


def extract_data_freshness() -> dict[str, str]:
    result = {
        "main_price_date": "",
        "report_ready": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "stock_monitor_date": "",
        "warrant_flow_date": "",
    }

    if DATA_FRESHNESS_CSV.exists():
        try:
            df = pd.read_csv(DATA_FRESHNESS_CSV, dtype=str)
            if not df.empty:
                row = df.iloc[0].to_dict()
                result["main_price_date"] = normalize_date(row.get("main_price_date", ""))
                result["report_ready"] = str(row.get("report_ready", "")).strip()
                result["all_candidates_date"] = normalize_date(row.get("all_candidates_date", ""))
                result["official_price_fetch_date"] = normalize_date(row.get("official_price_fetch_date", ""))
                result["stock_monitor_date"] = normalize_date(row.get("stock_monitor_price_date", ""))
                result["warrant_flow_date"] = normalize_date(row.get("warrant_flow_date", ""))
                return result
        except Exception:
            pass

    if DATA_FRESHNESS_MD.exists():
        text = DATA_FRESHNESS_MD.read_text(encoding="utf-8", errors="ignore")

        m = re.search(r"主資料日期[：:\s`]*([0-9/\-]{8,10})", text)
        if m:
            result["main_price_date"] = normalize_date(m.group(1))

        m = re.search(r"是否可產出正式每日報告[：:\s`]*(True|False|true|false)", text)
        if m:
            result["report_ready"] = m.group(1)

    return result


def get_artifact_commit_sha() -> str:
    env_sha = os.environ.get("ARTIFACT_COMMIT_SHA", "").strip()

    if env_sha:
        return env_sha

    code, out, _ = run_command(["git", "rev-parse", "HEAD"])
    if code == 0:
        return out.strip()

    return ""


def curl_head(url: str) -> dict[str, Any]:
    code, out, err = run_command(
        ["curl", "-I", "-L", "--max-time", "30", url],
        timeout=45,
    )

    status_code = ""

    for line in out.splitlines():
        if line.startswith("HTTP/"):
            parts = line.split()
            if len(parts) >= 2:
                status_code = parts[1]

    return {
        "command": f"curl -I -L --max-time 30 {url}",
        "returncode": code,
        "http_status": status_code,
        "stdout": out,
        "stderr": err,
        "ok": code == 0 and status_code == "200",
    }


def curl_body(url: str) -> dict[str, Any]:
    code, out, err = run_command(
        ["curl", "-L", "--max-time", "30", url],
        timeout=45,
    )

    contains_packet = "CHATGPT DAILY REPORT PACKET" in out
    contains_summary = "EMBEDDED SUMMARY REPORT" in out
    contains_full = "EMBEDDED FULL REPORT" in out

    return {
        "command": f"curl -L --max-time 30 {url}",
        "returncode": code,
        "stdout_head": "\n".join(out.splitlines()[:50]),
        "stderr": err,
        "contains_packet": contains_packet,
        "contains_summary": contains_summary,
        "contains_full": contains_full,
        "ok": code == 0 and contains_packet and contains_summary and contains_full,
    }


def curl_github_api_packet(url: str) -> dict[str, Any]:
    code, out, err = run_command(
        ["curl", "-L", "--max-time", "30", url],
        timeout=45,
    )

    decoded_text = ""
    api_parse_ok = False

    if code == 0:
        try:
            data = json.loads(out)
            content = data.get("content", "")
            encoding = data.get("encoding", "")

            if encoding == "base64" and content:
                decoded_bytes = base64.b64decode(content)
                decoded_text = decoded_bytes.decode("utf-8", errors="replace")
                api_parse_ok = True
        except Exception as exc:
            err = (err + "\n" + f"api decode failed: {exc}").strip()

    contains_packet = "CHATGPT DAILY REPORT PACKET" in decoded_text
    contains_summary = "EMBEDDED SUMMARY REPORT" in decoded_text
    contains_full = "EMBEDDED FULL REPORT" in decoded_text

    return {
        "command": f"curl -L --max-time 30 {url}",
        "returncode": code,
        "stdout_head": "\n".join(out.splitlines()[:50]),
        "decoded_head": "\n".join(decoded_text.splitlines()[:50]),
        "stderr": err,
        "api_parse_ok": api_parse_ok,
        "contains_packet": contains_packet,
        "contains_summary": contains_summary,
        "contains_full": contains_full,
        "ok": code == 0 and api_parse_ok and contains_packet and contains_summary and contains_full,
    }


def check_plain_packet_url(label: str, url: str) -> dict[str, Any]:
    head = curl_head(url)
    body = curl_body(url)

    return {
        "label": label,
        "url": url,
        "type": "plain",
        "head": head,
        "body": body,
        "ok": bool(head.get("ok")) and bool(body.get("ok")),
    }


def check_api_packet_url(label: str, url: str) -> dict[str, Any]:
    head = curl_head(url)
    body = curl_github_api_packet(url)

    return {
        "label": label,
        "url": url,
        "type": "github_api",
        "head": head,
        "body": body,
        "ok": bool(head.get("ok")) and bool(body.get("ok")),
    }


def choose_preferred(checks: list[dict[str, Any]]) -> str:
    for item in checks:
        if item.get("ok"):
            return str(item.get("url", ""))

    for item in checks:
        if item.get("label") == "packet_commit_raw_url":
            return str(item.get("url", ""))

    return ""


def build_readme(
    *,
    main_price_date: str,
    report_ready: str,
    commit_sha: str,
    packet_pages_url: str,
    packet_latest_raw_url: str,
    packet_commit_raw_url: str,
    packet_github_api_url: str,
    summary_latest_raw_url: str,
    full_latest_raw_url: str,
    daily_market_curated_pdf_pages_url: str,
    daily_market_curated_pdf_raw_url: str,
    daily_market_full_table_pdf_pages_url: str,
    daily_market_full_table_pdf_raw_url: str,
    fixed_pdf_validation_status: str,
    fixed_pdf_validation_raw_url: str,
    pdf_kline_status_pages_url: str,
    pdf_kline_status_raw_url: str,
    pdf_kline_policy: str,
    pdf_kline_status: str,
    pdf_kline_total_charts: Any,
    pdf_kline_local_price_redraw_count: Any,
    fundamental_catalyst_layer_raw_url: str,
    daily_signal_performance_summary_raw_url: str,
    daily_signal_performance_weekly_md_raw_url: str,
    daily_signal_performance_weekly_pdf_pages_url: str,
    daily_signal_performance_weekly_pdf_raw_url: str,
    daily_signal_performance_monthly_md_raw_url: str,
    daily_signal_performance_monthly_pdf_pages_url: str,
    daily_signal_performance_monthly_pdf_raw_url: str,
    warrant_market_report_md_raw_url: str,
    warrant_market_report_pdf_pages_url: str,
    warrant_market_report_pdf_raw_url: str,
    warrant_flow_by_stock_raw_url: str,
    warrant_sector_heat_raw_url: str,
    warrant_signal_performance_raw_url: str,
    market_regime_raw_url: str,
    market_risk_dashboard_md_raw_url: str,
    market_risk_dashboard_pdf_pages_url: str,
    market_risk_dashboard_pdf_raw_url: str,
    futures_options_indicators_raw_url: str,
    futures_options_source_status_raw_url: str,
    rules_pages_url: str,
    rules_raw_url: str,
    preferred_chatgpt_url: str,
    checks: list[dict[str, Any]],
) -> str:
    status_map = {item["label"]: item.get("ok") for item in checks}

    lines = [
        f"main_price_date={main_price_date}",
        f"report_ready={report_ready}",
        f"commit_sha={commit_sha}",
        f"preferred_chatgpt_url={preferred_chatgpt_url}",
        f"packet_pages_url={packet_pages_url}",
        f"packet_commit_raw_url={packet_commit_raw_url}",
        f"packet_latest_raw_url={packet_latest_raw_url}",
        f"packet_github_api_url={packet_github_api_url}",
        f"summary_latest_raw_url={summary_latest_raw_url}",
        f"full_latest_raw_url={full_latest_raw_url}",
        f"daily_market_curated_pdf_pages_url={daily_market_curated_pdf_pages_url}",
        f"daily_market_curated_pdf_raw_url={daily_market_curated_pdf_raw_url}",
        f"daily_market_full_table_pdf_pages_url={daily_market_full_table_pdf_pages_url}",
        f"daily_market_full_table_pdf_raw_url={daily_market_full_table_pdf_raw_url}",
        f"fixed_pdf_validation_status={fixed_pdf_validation_status}",
        f"fixed_pdf_validation_raw_url={fixed_pdf_validation_raw_url}",
        f"pdf_kline_status_pages_url={pdf_kline_status_pages_url}",
        f"pdf_kline_status_raw_url={pdf_kline_status_raw_url}",
        f"summary_pdf_kline_policy={pdf_kline_policy}",
        f"summary_pdf_kline_status={pdf_kline_status}",
        f"summary_pdf_kline_total_charts={pdf_kline_total_charts}",
        f"summary_pdf_kline_local_price_redraw_count={pdf_kline_local_price_redraw_count}",
        "summary_pdf_chart_path_and_chart_url_are_fallback_only=True",
        "do_not_label_summary_pdf_as_chart_path_version_or_image_download_failed=True",
        f"fundamental_catalyst_layer_raw_url={fundamental_catalyst_layer_raw_url}",
        f"daily_signal_performance_summary_raw_url={daily_signal_performance_summary_raw_url}",
        f"daily_signal_performance_weekly_md_raw_url={daily_signal_performance_weekly_md_raw_url}",
        f"daily_signal_performance_weekly_pdf_pages_url={daily_signal_performance_weekly_pdf_pages_url}",
        f"daily_signal_performance_weekly_pdf_raw_url={daily_signal_performance_weekly_pdf_raw_url}",
        f"daily_signal_performance_monthly_md_raw_url={daily_signal_performance_monthly_md_raw_url}",
        f"daily_signal_performance_monthly_pdf_pages_url={daily_signal_performance_monthly_pdf_pages_url}",
        f"daily_signal_performance_monthly_pdf_raw_url={daily_signal_performance_monthly_pdf_raw_url}",
        f"warrant_market_report_md_raw_url={warrant_market_report_md_raw_url}",
        f"warrant_market_report_pdf_pages_url={warrant_market_report_pdf_pages_url}",
        f"warrant_market_report_pdf_raw_url={warrant_market_report_pdf_raw_url}",
        f"warrant_flow_by_stock_raw_url={warrant_flow_by_stock_raw_url}",
        f"warrant_sector_heat_raw_url={warrant_sector_heat_raw_url}",
        f"warrant_signal_performance_raw_url={warrant_signal_performance_raw_url}",
        f"market_regime_raw_url={market_regime_raw_url}",
        f"market_risk_dashboard_md_raw_url={market_risk_dashboard_md_raw_url}",
        f"market_risk_dashboard_pdf_pages_url={market_risk_dashboard_pdf_pages_url}",
        f"market_risk_dashboard_pdf_raw_url={market_risk_dashboard_pdf_raw_url}",
        f"futures_options_indicators_raw_url={futures_options_indicators_raw_url}",
        f"futures_options_source_status_raw_url={futures_options_source_status_raw_url}",
        f"rules_pages_url={rules_pages_url}",
        f"rules_raw_url={rules_raw_url}",
        f"packet_pages_ok={status_map.get('packet_pages_url')}",
        f"packet_commit_raw_ok={status_map.get('packet_commit_raw_url')}",
        f"packet_latest_raw_ok={status_map.get('packet_latest_raw_url')}",
        f"packet_github_api_ok={status_map.get('packet_github_api_url')}",
        "read_order=packet_pages_url,packet_commit_raw_url,packet_latest_raw_url,packet_github_api_url",
        "",
        "RULES:",
        "1. Read this entry file first.",
        "2. Read rules_pages_url or rules_raw_url to load report format rules.",
        "3. Read preferred_chatgpt_url for the packet.",
        "4. If preferred_chatgpt_url fails, follow read_order.",
        "5. If the URL is packet_github_api_url, decode the JSON content field from base64 before reading the packet.",
        "6. If packet is readable, use EMBEDDED SUMMARY REPORT and EMBEDDED FULL REPORT as source of truth.",
        "7. For shareable PDFs, use daily_market_curated_pdf_pages_url and daily_market_full_table_pdf_pages_url first.",
        "8. For the summary PDF K-line charts, use summary_pdf_kline_policy/status/counts above. Do not downgrade the PDF to chart_path/image-download-failed if local_price_redraw_count is greater than 0.",
        "9. If all URLs fail, say tool reading failed. Do not say GitHub data is not updated.",
        "10. Do not use older report dates to recreate a newer report.",
        "",
    ]

    return "\n".join(lines)


def build_publish_check_md(
    *,
    main_price_date: str,
    report_ready: str,
    commit_sha: str,
    preferred_chatgpt_url: str,
    checks: list[dict[str, Any]],
    rules_pages_url: str,
    rules_raw_url: str,
    daily_market_curated_pdf_pages_url: str,
    daily_market_curated_pdf_raw_url: str,
    daily_market_full_table_pdf_pages_url: str,
    daily_market_full_table_pdf_raw_url: str,
    fixed_pdf_validation_status: str,
    fixed_pdf_validation_raw_url: str,
    pdf_kline_status_pages_url: str,
    pdf_kline_status_raw_url: str,
    pdf_kline_policy: str,
    pdf_kline_status: str,
    pdf_kline_total_charts: Any,
    pdf_kline_local_price_redraw_count: Any,
) -> str:
    lines: list[str] = []

    lines.append("# Report Publish Check")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append(f"- main_price_date: `{main_price_date}`")
    lines.append(f"- report_ready: `{report_ready}`")
    lines.append(f"- artifact_commit_sha: `{commit_sha}`")
    lines.append(f"- preferred_chatgpt_url: `{preferred_chatgpt_url}`")
    lines.append(f"- rules_pages_url: `{rules_pages_url}`")
    lines.append(f"- rules_raw_url: `{rules_raw_url}`")
    lines.append(f"- daily_market_curated_pdf_pages_url: `{daily_market_curated_pdf_pages_url}`")
    lines.append(f"- daily_market_curated_pdf_raw_url: `{daily_market_curated_pdf_raw_url}`")
    lines.append(f"- daily_market_full_table_pdf_pages_url: `{daily_market_full_table_pdf_pages_url}`")
    lines.append(f"- daily_market_full_table_pdf_raw_url: `{daily_market_full_table_pdf_raw_url}`")
    lines.append(f"- fixed_pdf_validation_status: `{fixed_pdf_validation_status}`")
    lines.append(f"- fixed_pdf_validation_raw_url: `{fixed_pdf_validation_raw_url}`")
    lines.append(f"- pdf_kline_status_pages_url: `{pdf_kline_status_pages_url}`")
    lines.append(f"- pdf_kline_status_raw_url: `{pdf_kline_status_raw_url}`")
    lines.append(f"- summary_pdf_kline_policy: `{pdf_kline_policy}`")
    lines.append(f"- summary_pdf_kline_status: `{pdf_kline_status}`")
    lines.append(f"- summary_pdf_kline_total_charts: `{pdf_kline_total_charts}`")
    lines.append(f"- summary_pdf_kline_local_price_redraw_count: `{pdf_kline_local_price_redraw_count}`")
    lines.append("")
    lines.append("## Read Order")
    lines.append("")
    lines.append("1. packet_pages_url")
    lines.append("2. packet_commit_raw_url")
    lines.append("3. packet_latest_raw_url")
    lines.append("4. packet_github_api_url")
    lines.append("")

    for item in checks:
        label = item.get("label", "")
        url = item.get("url", "")
        ok = item.get("ok", False)
        body = item.get("body", {})
        head = item.get("head", {})

        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"- ok: `{ok}`")
        lines.append(f"- type: `{item.get('type')}`")
        lines.append(f"- url: `{url}`")
        lines.append("")
        lines.append("### curl -I")
        lines.append("")
        lines.append("```text")
        lines.append(head.get("command", ""))
        lines.append(head.get("stdout", ""))
        if head.get("stderr"):
            lines.append("STDERR:")
            lines.append(head.get("stderr", ""))
        lines.append("```")
        lines.append("")
        lines.append("### curl -L | head -50")
        lines.append("")
        lines.append("```text")
        lines.append(body.get("command", ""))
        lines.append(body.get("stdout_head", ""))
        if body.get("decoded_head"):
            lines.append("")
            lines.append("DECODED_HEAD:")
            lines.append(body.get("decoded_head", ""))
        if body.get("stderr"):
            lines.append("STDERR:")
            lines.append(body.get("stderr", ""))
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def sync_docs_files() -> None:
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)

    if LATEST_PACKET.exists():
        DOCS_LATEST_PACKET.write_text(
            LATEST_PACKET.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    if RULES_LATEST.exists():
        RULES_DOCS.write_text(
            RULES_LATEST.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    if PDF_KLINE_STATUS_MD.exists():
        DOCS_PDF_KLINE_STATUS_MD.write_text(
            PDF_KLINE_STATUS_MD.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    if CURATED_REPORT_PDF.exists():
        DOCS_CURATED_REPORT_PDF.write_bytes(CURATED_REPORT_PDF.read_bytes())

    if FULL_TABLE_REPORT_PDF.exists():
        DOCS_FULL_TABLE_REPORT_PDF.write_bytes(FULL_TABLE_REPORT_PDF.read_bytes())

    if FIXED_PDF_VALIDATION_MD.exists():
        DOCS_FIXED_PDF_VALIDATION_MD.write_text(
            FIXED_PDF_VALIDATION_MD.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    if DAILY_SIGNAL_WEEKLY_PDF.exists():
        DOCS_DAILY_SIGNAL_WEEKLY_PDF.write_bytes(DAILY_SIGNAL_WEEKLY_PDF.read_bytes())

    if DAILY_SIGNAL_MONTHLY_PDF.exists():
        DOCS_DAILY_SIGNAL_MONTHLY_PDF.write_bytes(DAILY_SIGNAL_MONTHLY_PDF.read_bytes())


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)

    sync_docs_files()

    freshness = extract_data_freshness()
    packet_manifest = read_json(PACKET_MANIFEST_JSON)
    fixed_pdf_manifest = read_json(FIXED_PDF_MANIFEST_JSON)
    fixed_pdf_validation = read_json(FIXED_PDF_VALIDATION_JSON)

    main_price_date = freshness.get("main_price_date") or normalize_date(packet_manifest.get("main_price_date", ""))
    report_ready = freshness.get("report_ready") or str(packet_manifest.get("report_ready", "")).strip()

    if not main_price_date:
        raise RuntimeError("main_price_date is missing")

    if not report_ready:
        report_ready = "False"

    commit_sha = get_artifact_commit_sha()
    if not commit_sha:
        raise RuntimeError("artifact commit sha is missing")

    history_packet = HISTORY_REPORT_DIR / f"{main_price_date}_CHATGPT_DAILY_REPORT_PACKET.txt"

    packet_pages_url = pages_url("latest/chatgpt_daily_report_packet_latest.txt")
    packet_latest_raw_url = raw_url("main", LATEST_PACKET)
    packet_commit_raw_url = raw_url(commit_sha, history_packet)
    packet_github_api_url = github_api_url(LATEST_PACKET, ref="main")
    summary_latest_raw_url = raw_url("main", LATEST_SUMMARY_MD)
    full_latest_raw_url = raw_url("main", LATEST_FULL_MD)
    curated_pdf_info = fixed_pdf_manifest.get("curated_pdf", {})
    full_table_pdf_info = fixed_pdf_manifest.get("full_table_pdf", {})
    daily_market_curated_pdf_pages_url = curated_pdf_info.get("pages_url") or pages_url("latest/daily_market_curated_report_latest.pdf")
    daily_market_curated_pdf_raw_url = curated_pdf_info.get("raw_url") or raw_url("main", CURATED_REPORT_PDF)
    daily_market_full_table_pdf_pages_url = full_table_pdf_info.get("pages_url") or pages_url("latest/daily_market_full_table_report_latest.pdf")
    daily_market_full_table_pdf_raw_url = full_table_pdf_info.get("raw_url") or raw_url("main", FULL_TABLE_REPORT_PDF)
    fixed_pdf_validation_status = fixed_pdf_validation.get("status", "")
    fixed_pdf_validation_raw_url = raw_url("main", FIXED_PDF_VALIDATION_MD)
    pdf_kline_status_pages_url = pages_url("latest/pdf_kline_chart_status_latest.md")
    pdf_kline_status_raw_url = raw_url("main", PDF_KLINE_STATUS_MD)
    pdf_kline_status_json = read_json(PDF_KLINE_STATUS_JSON).get("summary", {})
    pdf_kline_policy = (
        pdf_kline_status_json.get("policy")
        or packet_manifest.get("summary_pdf_kline_policy")
        or "local_price_redraw_first"
    )
    pdf_kline_status = pdf_kline_status_json.get("status") or packet_manifest.get("summary_pdf_kline_status", "")
    pdf_kline_total_charts = pdf_kline_status_json.get(
        "total_charts",
        packet_manifest.get("summary_pdf_kline_total_charts", 0),
    )
    pdf_kline_local_price_redraw_count = pdf_kline_status_json.get(
        "local_price_redraw_count",
        packet_manifest.get("summary_pdf_kline_local_price_redraw_count", 0),
    )
    fundamental_catalyst_layer_raw_url = raw_url("main", FUNDAMENTAL_CATALYST_MD)
    daily_signal_performance_summary_raw_url = raw_url("main", DAILY_SIGNAL_SUMMARY_MD)
    daily_signal_performance_weekly_md_raw_url = raw_url("main", DAILY_SIGNAL_WEEKLY_MD)
    daily_signal_performance_weekly_pdf_pages_url = pages_url("latest/daily_signal_performance_weekly_latest.pdf")
    daily_signal_performance_weekly_pdf_raw_url = raw_url("main", DAILY_SIGNAL_WEEKLY_PDF)
    daily_signal_performance_monthly_md_raw_url = raw_url("main", DAILY_SIGNAL_MONTHLY_MD)
    daily_signal_performance_monthly_pdf_pages_url = pages_url("latest/daily_signal_performance_monthly_latest.pdf")
    daily_signal_performance_monthly_pdf_raw_url = raw_url("main", DAILY_SIGNAL_MONTHLY_PDF)
    warrant_market_report_md_raw_url = raw_url("main", WARRANT_MARKET_MD)
    warrant_market_report_pdf_pages_url = pages_url("latest/warrant_market_report_latest.pdf")
    warrant_market_report_pdf_raw_url = raw_url("main", WARRANT_MARKET_PDF)
    warrant_flow_by_stock_raw_url = raw_url("main", WARRANT_FLOW_BY_STOCK_CSV)
    warrant_sector_heat_raw_url = raw_url("main", WARRANT_SECTOR_HEAT_CSV)
    warrant_signal_performance_raw_url = raw_url("main", WARRANT_SIGNAL_PERFORMANCE_MD)
    market_regime_raw_url = raw_url("main", MARKET_REGIME_CSV)
    market_risk_dashboard_md_raw_url = raw_url("main", MARKET_RISK_DASHBOARD_MD)
    market_risk_dashboard_pdf_pages_url = pages_url("latest/market_risk_dashboard_latest.pdf")
    market_risk_dashboard_pdf_raw_url = raw_url("main", MARKET_RISK_DASHBOARD_PDF)
    futures_options_indicators_raw_url = raw_url("main", FUTURES_OPTIONS_INDICATORS_CSV)
    futures_options_source_status_raw_url = raw_url("main", FUTURES_OPTIONS_SOURCE_STATUS_MD)

    rules_pages_url = pages_url("latest/CHATGPT_DAILY_REPORT_RULES.txt")
    rules_raw_url = raw_url("main", RULES_LATEST)

    checks = [
        check_plain_packet_url("packet_pages_url", packet_pages_url),
        check_plain_packet_url("packet_commit_raw_url", packet_commit_raw_url),
        check_plain_packet_url("packet_latest_raw_url", packet_latest_raw_url),
        check_api_packet_url("packet_github_api_url", packet_github_api_url),
    ]

    preferred = choose_preferred(checks)

    readme = build_readme(
        main_price_date=main_price_date,
        report_ready=report_ready,
        commit_sha=commit_sha,
        packet_pages_url=packet_pages_url,
        packet_latest_raw_url=packet_latest_raw_url,
        packet_commit_raw_url=packet_commit_raw_url,
        packet_github_api_url=packet_github_api_url,
        summary_latest_raw_url=summary_latest_raw_url,
        full_latest_raw_url=full_latest_raw_url,
        daily_market_curated_pdf_pages_url=daily_market_curated_pdf_pages_url,
        daily_market_curated_pdf_raw_url=daily_market_curated_pdf_raw_url,
        daily_market_full_table_pdf_pages_url=daily_market_full_table_pdf_pages_url,
        daily_market_full_table_pdf_raw_url=daily_market_full_table_pdf_raw_url,
        fixed_pdf_validation_status=fixed_pdf_validation_status,
        fixed_pdf_validation_raw_url=fixed_pdf_validation_raw_url,
        pdf_kline_status_pages_url=pdf_kline_status_pages_url,
        pdf_kline_status_raw_url=pdf_kline_status_raw_url,
        pdf_kline_policy=pdf_kline_policy,
        pdf_kline_status=pdf_kline_status,
        pdf_kline_total_charts=pdf_kline_total_charts,
        pdf_kline_local_price_redraw_count=pdf_kline_local_price_redraw_count,
        fundamental_catalyst_layer_raw_url=fundamental_catalyst_layer_raw_url,
        daily_signal_performance_summary_raw_url=daily_signal_performance_summary_raw_url,
        daily_signal_performance_weekly_md_raw_url=daily_signal_performance_weekly_md_raw_url,
        daily_signal_performance_weekly_pdf_pages_url=daily_signal_performance_weekly_pdf_pages_url,
        daily_signal_performance_weekly_pdf_raw_url=daily_signal_performance_weekly_pdf_raw_url,
        daily_signal_performance_monthly_md_raw_url=daily_signal_performance_monthly_md_raw_url,
        daily_signal_performance_monthly_pdf_pages_url=daily_signal_performance_monthly_pdf_pages_url,
        daily_signal_performance_monthly_pdf_raw_url=daily_signal_performance_monthly_pdf_raw_url,
        warrant_market_report_md_raw_url=warrant_market_report_md_raw_url,
        warrant_market_report_pdf_pages_url=warrant_market_report_pdf_pages_url,
        warrant_market_report_pdf_raw_url=warrant_market_report_pdf_raw_url,
        warrant_flow_by_stock_raw_url=warrant_flow_by_stock_raw_url,
        warrant_sector_heat_raw_url=warrant_sector_heat_raw_url,
        warrant_signal_performance_raw_url=warrant_signal_performance_raw_url,
        market_regime_raw_url=market_regime_raw_url,
        market_risk_dashboard_md_raw_url=market_risk_dashboard_md_raw_url,
        market_risk_dashboard_pdf_pages_url=market_risk_dashboard_pdf_pages_url,
        market_risk_dashboard_pdf_raw_url=market_risk_dashboard_pdf_raw_url,
        futures_options_indicators_raw_url=futures_options_indicators_raw_url,
        futures_options_source_status_raw_url=futures_options_source_status_raw_url,
        rules_pages_url=rules_pages_url,
        rules_raw_url=rules_raw_url,
        preferred_chatgpt_url=preferred,
        checks=checks,
    )

    README_TXT.write_text(readme, encoding="utf-8")
    DOCS_README_TXT.write_text(readme, encoding="utf-8")
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (HISTORY_REPORT_DIR / f"{main_price_date}_READ_ME_FIRST_DAILY_REPORT.txt").write_text(
        readme,
        encoding="utf-8",
    )

    publish_check_md = build_publish_check_md(
        main_price_date=main_price_date,
        report_ready=report_ready,
        commit_sha=commit_sha,
        preferred_chatgpt_url=preferred,
        checks=checks,
        rules_pages_url=rules_pages_url,
        rules_raw_url=rules_raw_url,
        daily_market_curated_pdf_pages_url=daily_market_curated_pdf_pages_url,
        daily_market_curated_pdf_raw_url=daily_market_curated_pdf_raw_url,
        daily_market_full_table_pdf_pages_url=daily_market_full_table_pdf_pages_url,
        daily_market_full_table_pdf_raw_url=daily_market_full_table_pdf_raw_url,
        fixed_pdf_validation_status=fixed_pdf_validation_status,
        fixed_pdf_validation_raw_url=fixed_pdf_validation_raw_url,
        pdf_kline_status_pages_url=pdf_kline_status_pages_url,
        pdf_kline_status_raw_url=pdf_kline_status_raw_url,
        pdf_kline_policy=pdf_kline_policy,
        pdf_kline_status=pdf_kline_status,
        pdf_kline_total_charts=pdf_kline_total_charts,
        pdf_kline_local_price_redraw_count=pdf_kline_local_price_redraw_count,
    )

    PUBLISH_CHECK_MD.write_text(publish_check_md, encoding="utf-8")

    publish_check_json = {
        "generated_at": now_text(),
        "main_price_date": main_price_date,
        "report_ready": report_ready,
        "commit_sha": commit_sha,
        "preferred_chatgpt_url": preferred,
        "read_order": [
            "packet_pages_url",
            "packet_commit_raw_url",
            "packet_latest_raw_url",
            "packet_github_api_url",
        ],
        "packet_pages_url": packet_pages_url,
        "packet_latest_raw_url": packet_latest_raw_url,
        "packet_commit_raw_url": packet_commit_raw_url,
        "packet_github_api_url": packet_github_api_url,
        "summary_latest_raw_url": summary_latest_raw_url,
        "full_latest_raw_url": full_latest_raw_url,
        "daily_market_curated_pdf_pages_url": daily_market_curated_pdf_pages_url,
        "daily_market_curated_pdf_raw_url": daily_market_curated_pdf_raw_url,
        "daily_market_full_table_pdf_pages_url": daily_market_full_table_pdf_pages_url,
        "daily_market_full_table_pdf_raw_url": daily_market_full_table_pdf_raw_url,
        "fixed_pdf_validation_status": fixed_pdf_validation_status,
        "fixed_pdf_validation_raw_url": fixed_pdf_validation_raw_url,
        "pdf_kline_status_pages_url": pdf_kline_status_pages_url,
        "pdf_kline_status_raw_url": pdf_kline_status_raw_url,
        "summary_pdf_kline_policy": pdf_kline_policy,
        "summary_pdf_kline_status": pdf_kline_status,
        "summary_pdf_kline_total_charts": pdf_kline_total_charts,
        "summary_pdf_kline_local_price_redraw_count": pdf_kline_local_price_redraw_count,
        "summary_pdf_chart_path_and_chart_url_are_fallback_only": True,
        "do_not_label_summary_pdf_as_chart_path_version_or_image_download_failed": True,
        "fundamental_catalyst_layer_raw_url": fundamental_catalyst_layer_raw_url,
        "daily_signal_performance_summary_raw_url": daily_signal_performance_summary_raw_url,
        "daily_signal_performance_weekly_md_raw_url": daily_signal_performance_weekly_md_raw_url,
        "daily_signal_performance_weekly_pdf_pages_url": daily_signal_performance_weekly_pdf_pages_url,
        "daily_signal_performance_weekly_pdf_raw_url": daily_signal_performance_weekly_pdf_raw_url,
        "daily_signal_performance_monthly_md_raw_url": daily_signal_performance_monthly_md_raw_url,
        "daily_signal_performance_monthly_pdf_pages_url": daily_signal_performance_monthly_pdf_pages_url,
        "daily_signal_performance_monthly_pdf_raw_url": daily_signal_performance_monthly_pdf_raw_url,
        "warrant_market_report_md_raw_url": warrant_market_report_md_raw_url,
        "warrant_market_report_pdf_pages_url": warrant_market_report_pdf_pages_url,
        "warrant_market_report_pdf_raw_url": warrant_market_report_pdf_raw_url,
        "warrant_flow_by_stock_raw_url": warrant_flow_by_stock_raw_url,
        "warrant_sector_heat_raw_url": warrant_sector_heat_raw_url,
        "warrant_signal_performance_raw_url": warrant_signal_performance_raw_url,
        "market_regime_raw_url": market_regime_raw_url,
        "market_risk_dashboard_md_raw_url": market_risk_dashboard_md_raw_url,
        "market_risk_dashboard_pdf_pages_url": market_risk_dashboard_pdf_pages_url,
        "market_risk_dashboard_pdf_raw_url": market_risk_dashboard_pdf_raw_url,
        "futures_options_indicators_raw_url": futures_options_indicators_raw_url,
        "futures_options_source_status_raw_url": futures_options_source_status_raw_url,
        "rules_pages_url": rules_pages_url,
        "rules_raw_url": rules_raw_url,
        "checks": checks,
    }

    PUBLISH_CHECK_JSON.write_text(
        json.dumps(publish_check_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Saved: {README_TXT}")
    print(f"Saved: {DOCS_README_TXT}")
    print(f"Saved: {PUBLISH_CHECK_MD}")
    print(f"Saved: {PUBLISH_CHECK_JSON}")
    print(f"preferred_chatgpt_url={preferred}")
    print(f"rules_pages_url={rules_pages_url}")
    print(f"rules_raw_url={rules_raw_url}")

    for item in checks:
        print(f"{item.get('label')} ok={item.get('ok')} url={item.get('url')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
