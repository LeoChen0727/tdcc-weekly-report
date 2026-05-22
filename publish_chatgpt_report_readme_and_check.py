from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os
import re
import subprocess
from typing import Any

import pandas as pd


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}"

LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
PACKET_MANIFEST_JSON = LATEST_DIR / "chatgpt_daily_report_packet_manifest.json"

README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
PUBLISH_CHECK_MD = LATEST_DIR / "report_publish_check_latest.md"
PUBLISH_CHECK_JSON = LATEST_DIR / "report_publish_check_latest.json"

LATEST_PACKET = LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
LATEST_SUMMARY_MD = LATEST_DIR / "daily_market_summary_latest.md"
LATEST_FULL_MD = LATEST_DIR / "daily_market_full_latest.md"


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


def run_command(args: list[str], timeout: int = 30) -> tuple[int, str, str]:
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
    code, out, err = run_command(["curl", "-I", "-L", "--max-time", "30", url], timeout=40)

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


def curl_body_head(url: str, lines: int = 50) -> dict[str, Any]:
    code, out, err = run_command(["curl", "-L", "--max-time", "30", url], timeout=40)

    head_lines = "\n".join(out.splitlines()[:lines])
    contains_packet = "CHATGPT DAILY REPORT PACKET" in out
    contains_summary = "EMBEDDED SUMMARY REPORT" in out
    contains_full = "EMBEDDED FULL REPORT" in out

    return {
        "command": f"curl -L --max-time 30 {url} | head -{lines}",
        "returncode": code,
        "stdout_head": head_lines,
        "stderr": err,
        "contains_packet": contains_packet,
        "contains_summary": contains_summary,
        "contains_full": contains_full,
        "ok": code == 0 and contains_packet and contains_summary and contains_full,
    }


def check_url(url: str) -> dict[str, Any]:
    head = curl_head(url)
    body = curl_body_head(url, lines=50)

    return {
        "url": url,
        "head": head,
        "body_head": body,
        "ok": bool(head.get("ok")) and bool(body.get("ok")),
    }


def build_readme(
    *,
    main_price_date: str,
    report_ready: str,
    commit_sha: str,
    packet_latest_raw_url: str,
    packet_commit_raw_url: str,
    summary_latest_raw_url: str,
    full_latest_raw_url: str,
    preferred_chatgpt_url: str,
    latest_ok: bool,
    commit_ok: bool,
) -> str:
    lines = [
        f"main_price_date={main_price_date}",
        f"report_ready={report_ready}",
        f"commit_sha={commit_sha}",
        f"preferred_chatgpt_url={preferred_chatgpt_url}",
        f"packet_latest_raw_url={packet_latest_raw_url}",
        f"packet_commit_raw_url={packet_commit_raw_url}",
        f"summary_latest_raw_url={summary_latest_raw_url}",
        f"full_latest_raw_url={full_latest_raw_url}",
        f"packet_latest_raw_ok={latest_ok}",
        f"packet_commit_raw_ok={commit_ok}",
        "",
        "RULES:",
        "1. Read preferred_chatgpt_url first.",
        "2. If preferred_chatgpt_url fails, try packet_commit_raw_url, then packet_latest_raw_url.",
        "3. If packet is readable, use EMBEDDED SUMMARY REPORT and EMBEDDED FULL REPORT as source of truth.",
        "4. If GitHub raw reading fails, say tool reading failed. Do not say GitHub data is not updated.",
        "5. Do not use older report dates to recreate a newer report.",
        "",
    ]

    return "\n".join(lines)


def build_publish_check_md(
    *,
    main_price_date: str,
    report_ready: str,
    commit_sha: str,
    packet_latest_raw_url: str,
    packet_commit_raw_url: str,
    preferred_chatgpt_url: str,
    latest_check: dict[str, Any],
    commit_check: dict[str, Any],
) -> str:
    lines: list[str] = []

    lines.append("# Report Publish Check")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append(f"- main_price_date: `{main_price_date}`")
    lines.append(f"- report_ready: `{report_ready}`")
    lines.append(f"- artifact_commit_sha: `{commit_sha}`")
    lines.append(f"- preferred_chatgpt_url: `{preferred_chatgpt_url}`")
    lines.append("")
    lines.append("## URLs")
    lines.append("")
    lines.append(f"- packet_latest_raw_url: `{packet_latest_raw_url}`")
    lines.append(f"- packet_commit_raw_url: `{packet_commit_raw_url}`")
    lines.append("")
    lines.append("## Latest Raw Check")
    lines.append("")
    lines.append(f"- ok: `{latest_check.get('ok')}`")
    lines.append(f"- URL: `{latest_check.get('url')}`")
    lines.append("")
    lines.append("### curl -I packet_latest_raw_url")
    lines.append("")
    lines.append("```text")
    lines.append(latest_check["head"].get("command", ""))
    lines.append(latest_check["head"].get("stdout", ""))
    if latest_check["head"].get("stderr"):
        lines.append("STDERR:")
        lines.append(latest_check["head"].get("stderr", ""))
    lines.append("```")
    lines.append("")
    lines.append("### curl -L packet_latest_raw_url | head -50")
    lines.append("")
    lines.append("```text")
    lines.append(latest_check["body_head"].get("command", ""))
    lines.append(latest_check["body_head"].get("stdout_head", ""))
    if latest_check["body_head"].get("stderr"):
        lines.append("STDERR:")
        lines.append(latest_check["body_head"].get("stderr", ""))
    lines.append("```")
    lines.append("")
    lines.append("## Commit Raw Check")
    lines.append("")
    lines.append(f"- ok: `{commit_check.get('ok')}`")
    lines.append(f"- URL: `{commit_check.get('url')}`")
    lines.append("")
    lines.append("### curl -I packet_commit_raw_url")
    lines.append("")
    lines.append("```text")
    lines.append(commit_check["head"].get("command", ""))
    lines.append(commit_check["head"].get("stdout", ""))
    if commit_check["head"].get("stderr"):
        lines.append("STDERR:")
        lines.append(commit_check["head"].get("stderr", ""))
    lines.append("```")
    lines.append("")
    lines.append("### curl -L packet_commit_raw_url | head -50")
    lines.append("")
    lines.append("```text")
    lines.append(commit_check["body_head"].get("command", ""))
    lines.append(commit_check["body_head"].get("stdout_head", ""))
    if commit_check["body_head"].get("stderr"):
        lines.append("STDERR:")
        lines.append(commit_check["body_head"].get("stderr", ""))
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    freshness = extract_data_freshness()
    packet_manifest = read_json(PACKET_MANIFEST_JSON)

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

    packet_latest_raw_url = raw_url("main", LATEST_PACKET)
    packet_commit_raw_url = raw_url(commit_sha, history_packet)
    summary_latest_raw_url = raw_url("main", LATEST_SUMMARY_MD)
    full_latest_raw_url = raw_url("main", LATEST_FULL_MD)

    latest_check = check_url(packet_latest_raw_url)
    commit_check = check_url(packet_commit_raw_url)

    latest_ok = bool(latest_check.get("ok"))
    commit_ok = bool(commit_check.get("ok"))

    if latest_ok:
        preferred = packet_latest_raw_url
    elif commit_ok:
        preferred = packet_commit_raw_url
    else:
        preferred = packet_commit_raw_url

    readme = build_readme(
        main_price_date=main_price_date,
        report_ready=report_ready,
        commit_sha=commit_sha,
        packet_latest_raw_url=packet_latest_raw_url,
        packet_commit_raw_url=packet_commit_raw_url,
        summary_latest_raw_url=summary_latest_raw_url,
        full_latest_raw_url=full_latest_raw_url,
        preferred_chatgpt_url=preferred,
        latest_ok=latest_ok,
        commit_ok=commit_ok,
    )

    README_TXT.write_text(readme, encoding="utf-8")

    publish_check_md = build_publish_check_md(
        main_price_date=main_price_date,
        report_ready=report_ready,
        commit_sha=commit_sha,
        packet_latest_raw_url=packet_latest_raw_url,
        packet_commit_raw_url=packet_commit_raw_url,
        preferred_chatgpt_url=preferred,
        latest_check=latest_check,
        commit_check=commit_check,
    )

    PUBLISH_CHECK_MD.write_text(publish_check_md, encoding="utf-8")

    publish_check_json = {
        "generated_at": now_text(),
        "main_price_date": main_price_date,
        "report_ready": report_ready,
        "commit_sha": commit_sha,
        "packet_latest_raw_url": packet_latest_raw_url,
        "packet_commit_raw_url": packet_commit_raw_url,
        "summary_latest_raw_url": summary_latest_raw_url,
        "full_latest_raw_url": full_latest_raw_url,
        "preferred_chatgpt_url": preferred,
        "packet_latest_raw_ok": latest_ok,
        "packet_commit_raw_ok": commit_ok,
        "latest_check": latest_check,
        "commit_check": commit_check,
    }

    PUBLISH_CHECK_JSON.write_text(
        json.dumps(publish_check_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Saved: {README_TXT}")
    print(f"Saved: {PUBLISH_CHECK_MD}")
    print(f"Saved: {PUBLISH_CHECK_JSON}")
    print(f"preferred_chatgpt_url={preferred}")
    print(f"packet_latest_raw_ok={latest_ok}")
    print(f"packet_commit_raw_ok={commit_ok}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
